import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/courses")
time.sleep(3)

#print(len(driver.find_elements("class name", "nav-link")))

driver.find_elements("class name", "nav-link")[3].click() #Ищем полный список совподающих элементов и нажимаем на 2ой с нуля
time.sleep(5)


