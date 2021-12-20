import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/find_link_text'

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    new_link = browser.find_element(By.LINK_TEXT, link_text)
    new_link.click()
    input1 = browser.find_element('name', 'first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element('name', 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()
    time.sleep(20)

