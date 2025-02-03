import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load Configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")
BASE_URL = config["settings"]["base_url"]
USERNAME = config["settings"]["username"]
PASSWORD = config["settings"]["password"]

# Setup WebDriver Fixture
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # Change to Firefox() if needed
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Test Login Functionality
def test_valid_login(driver):
    driver.get(BASE_URL)
    
    # Locate Elements
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Perform Login
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    login_button.click()

    # Verify Successful Login
    assert "Dashboard" in driver.title

# Test Google Search
def test_google_search(driver):
    driver.get("https://www.google.com")

    # Locate Search Box
    search_box = driver.find_element(By.NAME, "q")

    # Perform Search
    search_box.send_keys("Selenium automation")
    search_box.send_keys(Keys.RETURN)

    # Verify Search Results
    assert "Selenium" in driver.title

# Run tests with HTML report
if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html", "--self-contained-html"])
