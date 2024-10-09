
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

wait = WebDriverWait(driver, 15, poll_frequency=1) #15 - сколько жадть ожидаемого условияб poll - как часто запрашивать

driver.get("https://demoqa.com/dynamic-properties")

# visible_after_button = ("xpath", "//button[@id='visibleAfter']")
# button = wait.until(EC.visibility_of_element_located(visible_after_button))
# button.click()

enable_in_seconds = ("xpath", "//button[@id='enableAfter']")
button = wait.until(EC.element_to_be_clickable(enable_in_seconds))
button.click()
