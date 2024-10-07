import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru/ru/login")
time.sleep(3)

driver.find_element(By.ID, "loginformsubmit").click()






#print(type(driver.find_element("id", "loginformsubmit")))