from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Install Webdriver
service = Service(ChromeDriverManager().install())
 
with webdriver.Chrome(service=service) as driver:
    url = 'https://www.crawler-test.com'
    driver.get(url)
    title = driver.title
    print(title)