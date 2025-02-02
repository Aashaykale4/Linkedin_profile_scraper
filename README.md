# LinkedIn Profile Scraper API

## 📌 Project Description
This is a **Flask-based API** that uses **Selenium** to log in to LinkedIn, visit a user’s profile, and extract their profile URL. It automates the process of **web scraping LinkedIn** using browser automation.

---

## 🔹 Tech Stack Used
- **Python** (Flask for API, Selenium for automation)
- **Selenium WebDriver** (ChromeDriver for scraping)
- **Flask** (For API handling)
- **Requests** (For making HTTP calls)

---

## 🚀 How to Use

### 1️⃣ Setup
- Install dependencies:
  ```bash
  pip install flask selenium requests
### 2️⃣ Running the API
- Start the Flask server:
  ```bash
   python app.py
### 3️⃣ Sending a Request
- You can use Python or Postman to make a request.

  ```python
  import requests

  API_URL = "http://127.0.0.1:5000/scrape"
  data = {"linkedin_url": "https://www.linkedin.com/in/some-profile/"}

  response = requests.post(API_URL, json=data)
  print(response.json())
### 📌 Expected Output
    ``` json

      {
       "name":"example_name",
       "location":"example_location",
       "headline":"example_headline",
       "profile_picture": "https://media.licdn.com/dms/image/D4D03AQEcwCWnB3yGNQ/profile-photo-url.jpg"
      }

### 🎯 Next Steps
- ✅ Add **proxy rotation** to avoid bans.  
- ✅ Store profile pictures **in a database**.  
- ✅ Deploy on **AWS/GCP** for cloud use.
### 📌 [Documentation](https://www.notion.so/Project-LinkedIn-Profile-Scraper-API-18e67d84483080b18fdad04bf9332f79)
