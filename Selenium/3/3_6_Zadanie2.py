import time
import math
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, links, NoSuchElementException=None):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    browser.implicity_wait(10)
    browser.find_element(By.XPATH, '/html/body/header/nav/a[2]').click()

    browser.find_element(By.ID, "id_login_email").send_keys("") # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!LOGPASSWORD
    browser.find_element(By.ID, "id_login_password").send_keys("")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

    answer = math.log(int(time.time()))
    answer = str(answer)
    browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(answer)
    time.sleep(5)

    button = browser.find_element(By.XPATH, '//*[@id="ember507"]/div/section/div/div[1]/div[4]/button')
    button.click()
    time.sleep(5)

    massage = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert "successful" in massage.text
    print(massage)