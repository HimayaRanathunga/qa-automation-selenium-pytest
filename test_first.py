from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google_search():
  #open chrome browser 
  driver = webdriver.Chrome()

  #Google.com 
  driver.get("https://www.google.com")

  assert "Google" in driver.title

  print("Test Passed! Page title: ",driver.title)

  print("Test Passed! Page title:", driver.title)

  time.sleep(3)
  driver.quit()