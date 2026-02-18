from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.input_field_page import InputPage

import pytest




def test_text_input(driver):
    text = InputPage(driver)
    text.open()
    text.send_info(text.LOCATOR_TEXT, text.text_field)
    assert text.result() == 'This_is_a_string'
    # driver.get('https://www.qa-practice.com/elements/input/simple')
    # text_field = driver.find_element(By.CSS_SELECTOR, 'input[name=text_string]')
    # text_field.send_keys('This_is_a_string', Keys.ENTER)
    # result = driver.find_element(By.CSS_SELECTOR, '.result-text')
    # assert result.text == 'This_is_a_string'


def test_email_field(driver):
    email = InputPage(driver)
    email.open()
    email.click_element(email.LOCATOR_EMAIL)
    email.send_info(email.LOCATOR_INPUT_EMAIL, email.email_field)
    assert email.result() == 'example@gmail.com'
    # driver.get('https://www.qa-practice.com/elements/input/simple')
    # driver.find_element(By.LINK_TEXT, 'Email field').click()
    # email_field = driver.find_element(By.CSS_SELECTOR, 'input[name=email]')
    # email_field.send_keys('example@gmail.com', Keys.ENTER)
    # result = driver.find_element(By.CSS_SELECTOR, '.result-text')
    # assert result.text == 'example@gmail.com'


