from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



from .base_page import BasePage


class SelectPage(BasePage):

    LOCATOR_PLACE = (By.CSS_SELECTOR, 'select[name=choose_the_place_you_want_to_go]')
    LOCATOR_TRANSPORT = (By.CSS_SELECTOR, 'select[name=choose_how_you_want_to_get_there]')
    LOCATOR_TIME = (By.CSS_SELECTOR, 'select[name=choose_when_you_want_to_go]')
    LOCATOR_SUBMIT = (By.ID, 'submit-id-submit')
    LOCATOR_RESULT = (By.CLASS_NAME, 'result-text')

    URL = 'https://www.qa-practice.com/elements/select/single_select'

    def open(self):
        self.driver.get(self.URL)
        self.find((By.LINK_TEXT, 'Multiple selects')).click()


    def fill_form(self, place, transport, when_time):
        self.select_options(self.LOCATOR_PLACE, place)
        self.select_options(self.LOCATOR_TRANSPORT, transport)
        self.select_options(self.LOCATOR_TIME, when_time)

    def select_options(self, locator, text):
        Select(self.find(locator)).select_by_visible_text(text)

    def click_submit(self):
        self.find(self.LOCATOR_SUBMIT).click()

    def result(self, expected):
        self.wait.until(EC.text_to_be_present_in_element(self.LOCATOR_RESULT, expected))
        return self.find(self.LOCATOR_RESULT).text



