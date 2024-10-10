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
wait = WebDriverWait(driver, 30, poll_frequency=1) #15 - сколько жадть ожидаемого условияб poll - как часто запрашивать


# driver.get("https://dzen.ru")
# driver.save_screenshot("screen.png") # Скриншот окна