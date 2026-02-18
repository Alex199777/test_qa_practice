from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



from .base_page import BasePage

class InputPage(BasePage):

    URL = 'https://www.qa-practice.com/elements/input/simple'
    LOCATOR_TEXT = (By.CSS_SELECTOR, 'input[name=text_string]')
    LOCATOR_EMAIL = (By.LINK_TEXT, 'Email field')
    LOCATOR_INPUT_EMAIL = (By.CSS_SELECTOR, 'input[name=email]')
    LOCATOR_RESULT = (By.CSS_SELECTOR, '.result-text')
    text_field = 'This_is_a_string'
    email_field = 'example@gmail.com'


    def open(self):
        self.driver.get(self.URL)


    def click_element(self, element):
        self.find(element).click()

    def send_info(self, element, info):
        text = self.find(element)
        text.send_keys(info, Keys.ENTER)

    def result(self):
        return self.find(self.LOCATOR_RESULT).text

