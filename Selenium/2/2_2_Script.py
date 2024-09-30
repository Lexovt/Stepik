'''
import time
from selenium import webdriver
browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Script executing';alert('Robots at work');")
time.sleep(10)
'''
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button) #Скролит кнопку вверх страницы
browser.execute_script("window.scrollBy(0, 100);")
button.click()
time.sleep(10)
'''


#ZADANIE

import time
import math #Для функиции модуль
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

  # получаем число х из текста
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Ищем поле для ввода и вводим полученное число из формулы
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Выбрали чек бокс
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    browser.execute_script("window.scrollBy(0, 100);")  #скролим на 100 пикселей

    # Выбираем радиоБАТОН
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()

    # ищем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()

