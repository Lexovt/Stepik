
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestReg(unittest.TestCase):
    def test_reg1(self):
            link = "http://suninjuly.github.io/registration1.html"
            # link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element("xpath", "//input[@placeholder='Input your first name']")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
            input3.send_keys("aleks@gmail.com")
            time.sleep(2)
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            need_text = "Congratulations! You have successfully registered!"

            self.assertEqual(need_text, welcome_text, 'non text')

            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


    def test_reg2(self):

            #link = "http://suninjuly.github.io/registration1.html"
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element("xpath", "//input[@placeholder='Input your first name']")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
            input3.send_keys("aleks@gmail.com")
            time.sleep(2)
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            welcome_text = welcome_text_elt.text
            need_text = "Congratulations! You have successfully registered!"

            self.assertEqual(need_text, welcome_text, 'non text')


            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()