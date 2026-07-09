from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    driver = webdriver.Chrome()
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
    driver = webdriver.Chrome()
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