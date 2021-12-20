import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = 'http://suninjuly.github.io/file_input.html'

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name = firstname]')
    input1.send_keys('Masha')
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name = lastname]')
    input2.send_keys('Petrova')
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name = email]')
    input3.send_keys('masha@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'new.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(10)



