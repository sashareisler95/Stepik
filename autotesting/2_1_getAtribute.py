import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/get_attribute.html'


def func(x):
    return math.log(abs(12 * math.sin(x)))


with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    element = browser.find_element(By.CSS_SELECTOR, 'img[src="images/chest.png"]')
    x = int(element.get_attribute('valuex'))
    input_value = func(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(input_value)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(10)
