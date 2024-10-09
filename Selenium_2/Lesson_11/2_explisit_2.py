import time

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

wait = WebDriverWait(driver, 15, poll_frequency=1) #15 - сколько жадть ожидаемого условияб poll - как часто запрашивать

driver.get("https://the-internet.herokuapp.com/dynamic_controls")


###################################
# REMOVE_BUTTON = ("xpath","//button[text()='Remove']")
# driver.find_element(*REMOVE_BUTTON).click()
# wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
# print('ВСЁ ОК')
###################################


ENABLE_BUTTON = ("xpath","//button[text()='Enable']")
TEXT_FIELD = ("xpath","//input[@type='text']")

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click() #Нажимаем кнопку
time.sleep(2)
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys('HELLO!') #ВВодим текст
time.sleep(2)
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, 'HELLO!')) #Проверяем что текст в поле соответствует
time.sleep(2)
print('ВСЁ ОК')

