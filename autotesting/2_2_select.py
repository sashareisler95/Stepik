import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'


def find_sum(x, y):
    return x + y


with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    x = int(browser.find_element(By.ID, 'num1').text)
    y = int(browser.find_element(By.ID, 'num2').text)
    xy_sum = find_sum(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(xy_sum))
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(5)

