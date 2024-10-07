import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://mail.ru") #Открытие страницы
time.sleep(3)

driver.get("https://ya.ru")
time.sleep(3)

driver.back() #Переход назад по странице
time.sleep(3)

driver.forward() #Переход вперед по странице
time.sleep(3)

driver.refresh() #Перезагрузка страницы
time.sleep(3)