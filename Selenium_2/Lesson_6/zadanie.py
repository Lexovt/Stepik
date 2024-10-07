import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org")
time.sleep(3)

driver.find_elements("class name", "central-textlogo__image")
driver.find_elements("id", "searchInput")
driver.find_elements("class name", "pure-button pure-button-primary-progressive")
driver.find_elements("tag name", "span")[1]