import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/registration1.html'

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder ="Input your first name"]')
    first_name.send_keys('Vasya')
    last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder ="Input your last name"]')
    last_name.send_keys('Petrov')
    email_input = browser.find_element(By.CSS_SELECTOR, '[placeholder ="Input your email"]')
    email_input.send_keys('vasya@mail.ru')
    button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert 'Congratulations! You have successfully registered!' == welcome_text
    time.sleep(5)

