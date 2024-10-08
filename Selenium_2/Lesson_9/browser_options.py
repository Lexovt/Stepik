import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager" # "eager" "normal"
# chrome_options.add_argument("--headless") # Запуск теста без интерфейса
# chrome_options.add_argument("--incognito") #Режим инкогнито
# chrome_options.add_argument("--ignore-certificate-errors") #Игнорирование ошибок сертификатов
chrome_options.add_argument("--window-size=1920,1080") #Размер окна браузера
# chrome_options.add_argument("--disable-cache") #Отключение кеширования
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.set_window_size(1980,1080) #Размер окна браузера (не рекомендуется)

start_time = time.time()

driver.get("https://www.freeconferencecall.com/ru/ru")

end_time = time.time()
result = end_time - start_time
print(result)

