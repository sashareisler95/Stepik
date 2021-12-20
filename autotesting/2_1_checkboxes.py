import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    func = calc(x)
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(func)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(10)
