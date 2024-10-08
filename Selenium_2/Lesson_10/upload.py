import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal" # "eager" "normal"
chrome_options.add_argument("--window-size=1920,1080") #Размер окна браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

############################################################
# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(2)
# upload_field = driver.find_element("xpath", "//input[@type='file']")
# upload_field.send_keys(f"{os.getcwd()}/downloads/2.pdf")
# time.sleep(3)
############################################################
driver.get("https://www.freeconferencecall.com/ru/ru/login")
time.sleep(3)

Login_field = driver.find_element("xpath", "//input[@id='login_email']")
Login_field.send_keys("selenium@ya.ru")
password_field = driver.find_element("xpath", "//input[@type='password']")
password_field.send_keys("123")

# agree_checkbox = driver.find_element("xpath", "//a[@id='gdpr_checkbox']")
# agree_checkbox.click()

submit_button = driver.find_element("xpath", "//button[@id='loginformsubmit']")
submit_button.click()
time.sleep(3)

driver.get("https://www.freeconferencecall.com/profile/settings?tab=wall-editor")
time.sleep(2)
upload_field = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys(f"{os.getcwd()}/downloads/001.png")
time.sleep(2)


