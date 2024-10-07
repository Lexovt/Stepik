import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org")

url = driver.current_url #Получаем и выводим на экран  Url страницы
print('Url страницы:', url)
assert url == "https://www.wikipedia123.org", "Ошибка в Url. Открыта не та страница"

current_title = driver.title
print('Текущий заголовок страницы:', current_title)  #Считываем и выводим заголовок страницы
assert current_title == "Wikipedia", "Некорректный заголовок страницы"

print(driver.page_source) #Выводит на экран содержимое (код страницы)

time.sleep(3)

