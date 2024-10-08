import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://the-internet.herokuapp.com/status_codes")
time.sleep(3)

link_cod = driver.find_elements("xpath", "//a")[2].click()
time.sleep(2)
driver.back()
time.sleep(2)

link_cod = driver.find_elements("xpath", "//a")[3].click()
time.sleep(2)
driver.back()
time.sleep(2)

link_cod = driver.find_elements("xpath", "//a")[4].click()
time.sleep(2)
driver.back()
time.sleep(2)

link_cod = driver.find_elements("xpath", "//a")[5].click()
time.sleep(2)
driver.back()
time.sleep(2)