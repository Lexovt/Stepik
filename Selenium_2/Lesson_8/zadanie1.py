import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
time.sleep(2)


full_name = driver.find_element("xpath", "//input[@id='userName']")
full_name.clear()
assert full_name.get_attribute("value") == ""
full_name.send_keys("Alexey Petrov")
assert "Alexey Petrov" in full_name.get_attribute("value")
time.sleep(2)

user_email = driver.find_element("xpath", "//input[@id='userEmail']")
user_email.clear()
assert user_email.get_attribute("value") == ""
user_email.send_keys("Alexey@mail.ru")
assert "Alexey@mail.ru" in user_email.get_attribute("value")
time.sleep(2)

current_Address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
current_Address.clear()
assert current_Address.get_attribute("value") == ""
current_Address.send_keys("Russia Moscow")
assert "Russia Moscow" in current_Address.get_attribute("value")
time.sleep(2)

permanent_Address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_Address.clear()
assert permanent_Address.get_attribute("value") == ""
permanent_Address.send_keys("Ulica Pushkina, Dom kolotushkina")
assert "Ulica Pushkina, Dom kolotushkina" in permanent_Address.get_attribute("value")
time.sleep(2)





