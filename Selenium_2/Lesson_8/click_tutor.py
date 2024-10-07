import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru/ru")
time.sleep(3)

login_button = driver.find_element("xpath", "//a[@id='login-desktop']")
login_button.click()

email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("aleks")
time.sleep(3)

lab_text = driver.find_elements("xpath", "//a[@id='formlink_1']")[1]
print(lab_text.get_attribute("text"))
time.sleep(3)