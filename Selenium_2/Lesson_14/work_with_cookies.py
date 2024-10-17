import time
import os
import pickle

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait #Отвечает за явное ожидание
from selenium.webdriver.support import expected_conditions as EC  #Отвечает за условия ожидания

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal" # "eager" "normal"
chrome_options.add_argument("--window-size=1920,1080") #Размер окна браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1) #15 - сколько жадть ожидаемого условияб poll - как часто запрашивать

driver.get("https://www.freeconferencecall.com/ru/ru/login")

# print(driver.get_cookie("country_code")) # получаем отдельное значение куки

# print(driver.get_cookies()) # получаем Все значения куки

# driver.add_cookie({               #Добавление новой куки
#     "name": "Example",
#     "value": "Perdushka"
# })
#
# print(driver.get_cookie("Example"))
# time.sleep(2)

########### Удаление всех куков
# before = driver.get_cookies()
# print(before)
#
# driver.delete_all_cookies()
#
# driver.add_cookie({
#     "name": "split",
#     "value": "QUERTY"
# })
#
# after = driver.get_cookies()
# print(after)
##################################

# LOGIN_FIELD = ("xpath","//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath","//input[@id='password']")
# SUBMIT_BUTTON = ("xpath","//button[@id='loginformsubmit']")
#
# driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("123")
# driver.find_element(*SUBMIT_BUTTON).click()

# pickle.dump(driver.get_cookies(), open(os.getcwd()+"/coockies/coockies.pkl", "wb"))
driver.delete_all_cookies()
coockies = pickle.load(open(os.getcwd()+"/coockies/coockies.pkl", "rb"))

for cookie in coockies:
    driver.add_cookie(cookie)
time.sleep(3)

driver.refresh() # Что бы данные обновились

time.sleep(3)