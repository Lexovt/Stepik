import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads",
    # "safebrowsing.enabled" : True #Скачивает файлы полностью
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.page_load_strategy = "eager" # "eager" "normal"
chrome_options.add_argument("--window-size=1920,1080") #Размер окна браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("http://the-internet.herokuapp.com/download")
time.sleep(2)

elements = driver.find_elements("xpath", "//a")
print(len(elements))
time.sleep(3)

for item  in elements[2:53]:
    item.click()