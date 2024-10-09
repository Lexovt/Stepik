from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal" # "eager" "normal"
chrome_options.add_argument("--window-size=1920,1080") #Размер окна браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/dynamic-properties")

visible_after_button = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*visible_after_button).click()
