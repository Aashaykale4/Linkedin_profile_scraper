import requests

# Replace with your actual LinkedIn profile URL
linkedin_url = "https://www.linkedin.com/in/imsks/"

data = {
    "url": linkedin_url
}


url = "http://127.0.0.1:5000/scrape"
response = requests.post(url, json=data)


if response.status_code != 200:
    print("Error:", response.status_code, response.text)
else:
    
    profile_data = response.json()
    print(profile_data)
