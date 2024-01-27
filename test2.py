from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Install Webdriver
service = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("--headless")
 
with webdriver.Chrome(service=service, options=chrome_options) as driver:
    url = 'https://steamcommunity.com/id/grandpasaurus/inventory/#730'
    driver.get(url)
    title = driver.title
    print(title)
    print(driver.page_source)
    #print to file
    with open('test.html', 'w') as f:
        f.write(driver.page_source)

    