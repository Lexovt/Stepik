from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math #Для функиции модуль

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#получаем число х из картинки
img = browser.find_element(By.CSS_SELECTOR, "#treasure")
x = img.get_attribute("valuex")
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