from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    return driver


def test_valid_login():
    driver = get_driver()
    driver.get("https://www.saucedemo.com")

    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(2)

    assert "inventory" in driver.current_url
    print("Login Test Passed! Current URL:", driver.current_url)

    driver.quit()


def test_invalid_login():
    driver = get_driver()
    driver.get("https://www.saucedemo.com")

    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("wrong_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("wrong_password")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Username and password do not match" in error_message.text
    print("Invalid Login Test Passed! Error shown:", error_message.text)

    driver.quit()