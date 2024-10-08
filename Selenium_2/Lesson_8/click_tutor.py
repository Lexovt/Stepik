import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru/ru")
time.sleep(3)

#Находим кнопку и нажимаем ее
login_button = driver.find_element("xpath", "//a[@id='login-desktop']")
login_button.click()

#Находим поле и вводим текст
email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("aleks")
time.sleep(3)
#Очистить поле ввода
email_field.clear()

time.sleep(2)
email_field.send_keys("ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ")

#Получите обратно на экран текст с поля ввода
#print(email_field.get_attribute("value"))
time.sleep(3)