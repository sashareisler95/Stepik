import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/execute_script.html'


def result_value(x):
    return math.log((abs(12 * math.sin(x))))


with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(result_value(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(10)

