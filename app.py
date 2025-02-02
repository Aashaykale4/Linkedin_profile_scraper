
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    service = Service(ChromeDriverManager().install())  
    driver = webdriver.Chrome(service=service, options=options)  
    return driver


def linkedin_login(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password + Keys.RETURN)
    time.sleep(5)  

#Authentication 
def scrape_linkedin_profile(url):
    driver = setup_driver()
    linkedin_login(driver, 'Your Linkedin email', 'Your Password')  
    driver.get(url)
    
    
    time.sleep(10)

    profile_info = {
        "name": "Not Found", 
        "headline": "Not Found", 
        "location": "Not Found", 
        "profile_picture": "Not Found"
    }

    try:
        
        profile_info["name"] = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.xHYsZLZSbJQeLwSuSgdHFVqcvSYjHlobs.inline.t-24.v-align-middle.break-words"))).text
    except Exception as e:
        print(f"Error extracting name: {e}")

    try:
        
        profile_info["headline"] = driver.find_element(By.CSS_SELECTOR, "div.text-body-medium.break-words").text
    except Exception as e:
        print(f"Error extracting headline: {e}")

    try:
        
        profile_info["location"] = driver.find_element(By.CSS_SELECTOR, "span.text-body-small.inline.t-black--light.break-words").text
    except Exception as e:
        print(f"Error extracting location: {e}")

    try:
        
        profile_picture_element = driver.find_element(By.CSS_SELECTOR, "img.pv-member-photo-modal__content-image.evi-image")
        
        
        profile_picture_url = profile_picture_element.get_attribute("src")
        
        profile_info["profile_picture"] = profile_picture_url if profile_picture_url else "Not Found"
    except Exception as e:
        print(f"Error extracting profile picture: {e}")

    driver.quit()
    return profile_info


@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.json
        linkedin_url = data.get("url")
        
        if not linkedin_url:
            return jsonify({"error": "No URL provided"}), 400

        profile_info = scrape_linkedin_profile(linkedin_url)
        return jsonify(profile_info)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
