
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

link = "https://stepik.org/lesson/236895/step/1"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.XPATH, '//*[@id="ember458"]').click()
    #time.sleep(5)

    browser.find_element(By.ID, "id_login_email").send_keys("")
    browser.find_element(By.ID, "id_login_password").send_keys("")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()


    time.sleep(5)


# def test_login_stepik(browser):


'''
import time
import math #Для функиции модуль
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://stepik.org/lesson/236895/step/1"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    #time.sleep(1)
    button = browser.find_element(By.XPATH, '//*[@id="ember458"]')
    button.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(5)
    browser.quit()
'''
