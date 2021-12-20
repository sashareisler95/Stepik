import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/alert_accept.html'


def func(x):
    return math.log(abs(12 * math.sin(x)))


with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element(By.ID, 'input_value').text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(func(x))
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(5)
