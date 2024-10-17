import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait #Отвечает за явное ожидание
from selenium.webdriver.support import expected_conditions as EC  #Отвечает за условия ожидания

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal" # "eager" "normal"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080") #Размер окна браузера
chrome_options.add_argument("--disable-blink-features=AutomationControlled") #Отключает видимость Драйвер мода
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.3") #Меняет User agent
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 30, poll_frequency=1) #15 - сколько жадть ожидаемого условияб poll - как часто запрашивать


# driver.get("https://dzen.ru")
# driver.save_screenshot("screen.png") # Скриншот окна

# driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
# time.sleep(3)


driver.get("https://whatismyipaddress.com/")

wait.until(EC.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6"))
driver.save_screenshot("screen.png") # Скриншот окна