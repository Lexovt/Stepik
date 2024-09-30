import time
import math #Для функиции модуль
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    # Получение текста из элемента
    x = num1.text

    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    # Получение текста из элемента

    y = num2.text
    z = int(x)+ int(y)
    # Вывод текста на экран
    print(x, ' ', y, ' ', z)


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z)) # ищем элемент

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()