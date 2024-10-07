import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://vk.com")
current_title = driver.title
print('Текущий заголовок страницы:', current_title)  #Считываем и выводим заголовок страницы

driver.get("https://ya.ru")
current_title_2 = driver.title
print('Текущий заголовок страницы:', current_title_2)
time.sleep(3)

driver.back()
current_title = driver.title
assert current_title_2 != current_title , "Вы не вернулись на страницу"

driver.refresh()
url = driver.current_url #Получаем и выводим на экран  Url страницы
print('Url страницы:', url)
time.sleep(3)

driver.forward()
url_2 = driver.current_url
assert url != url_2, "Адрес страницы не изменился"

time.sleep(3)


