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

driver.get("https://omayo.blogspot.com/")

TEXT_INVISIBLE = ("xpath","//div[@id='deletesuccess']")
TEXT_VISIBLE = ("xpath","//div[@id='delayedText']")
ENABLE_BUTTON = ("xpath","//input[@id='timerButton']")
DISABLED_BUTTON = ("xpath","//button[@id='myBtn']")
TRY_IT_BUTTON = ("xpath", "//button[text()='Try it']")

wait.until(EC.invisibility_of_element_located(TEXT_INVISIBLE))
print('Текст исчез')
time.sleep(2)

wait.until(EC.visibility_of_element_located(TEXT_VISIBLE))
print('Текст появился')
time.sleep(2)

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON))
print('Кнопка активна')
time.sleep(2)


wait.until(EC.visibility_of_element_located(TRY_IT_BUTTON,)).click()
time.sleep(2)
print('Кнопка нажата')
wait.until(EC.element_located_selection_state_to_be((DISABLED_BUTTON), False))
print('Кнопка неактивна')
time.sleep(2)