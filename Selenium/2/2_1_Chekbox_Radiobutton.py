'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math #Для функиции модуль

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#получаем число х из текста
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

#Ищем поле для ввода и вводим полученное число из формулы
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

#Выбрали чек бокс
option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
option1.click()

#Выбираем радиоБАТОН
option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
option1.click()

#ищем кнопку
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element(By.CSS_SELECTOR, "#peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

#проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

#проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

#проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл