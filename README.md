# 🛠️ Automated System Testing Framework

![Selenium](https://img.shields.io/badge/Selenium-Testing-green)
![PyTest](https://img.shields.io/badge/PyTest-Test%20Automation-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)

## 📖 Overview

This project is an **Automated System Testing Framework** built with **Selenium WebDriver** and **PyTest**. It automates web application testing by performing **login validation** and **search functionality testing**. The framework is designed to be configurable and scalable for different test scenarios.

## 🚀 Features

✅ Web UI automation using **Selenium WebDriver**  
✅ Uses **PyTest** for test execution and reporting  
✅ Supports **configurable test settings** using `config.ini`  
✅ Generates **detailed HTML test reports**  
✅ Single-file script for **ease of use**  

---

## 🏗️ Project Structure

automated_testing_framework/ │── test_automation.py # Main test script (login & search tests) │── config.ini # Config file for test settings │── requirements.txt # Required dependencies │── report.html # Test report (generated after execution) │── README.md # Documentation

yaml
Copy
Edit

---

## 🔧 Installation

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/your-username/automated-testing-framework.git
cd automated-testing-framework
2️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set up the configuration file
Edit config.ini with your base URL, username, and password.

ini
Copy
Edit
[settings]
base_url = https://example.com
username = testuser
password = testpassword
📌 Usage
Run all test cases
bash
Copy
Edit
python test_automation.py
or using PyTest:

bash
Copy
Edit
pytest --html=report.html --self-contained-html
🛠️ Test Cases Included
✅ 1. Login Test
Opens the web page.
Enters username & password from config.ini.
Clicks Login and verifies successful login.
✅ 2. Google Search Test
Navigates to Google.
Searches for "Selenium automation".
Verifies search results.
📊 Test Reports
After execution, an HTML report is generated:

bash
Copy
Edit
report.html
Open it in a browser to view test results.

📌 Future Improvements
🔹 Extend test coverage (logout, form validation, error handling).
🔹 Integrate with CI/CD (GitHub Actions, Jenkins).
🔹 Implement API testing using requests.

🤝 Contributing
Pull requests are welcome! Feel free to improve test cases or extend functionality.
