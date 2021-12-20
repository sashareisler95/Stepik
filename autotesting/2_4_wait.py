import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

# browser = webdriver.Chrome()


def func(x):
    return math.log(abs(12 * math.sin(x)))


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"Результаты не совпадают! Ожидали получить {expected_result}, а получили {actual_result}"


# try:
#     browser.maximize_window()
#     browser.get("http://suninjuly.github.io/explicit_wait2.html")
#     button = browser.find_element(By.ID, 'book')
#     price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#     button.click()
#     x = int(browser.find_element(By.ID, 'input_value').text)
#     input1 = browser.find_element(By.ID, 'answer')
#     input1.send_keys(func(x))
#     button2 = browser.find_element(By.ID, 'solve')
#     button2.click()
#     time.sleep(5)
#
# finally:
#     browser.quit()

test_input_text(11, 15)

