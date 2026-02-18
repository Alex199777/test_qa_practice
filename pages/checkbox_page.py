from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from .base_page import BasePage

class CheckboxPage(BasePage):

    URL = 'https://www.qa-practice.com/elements/checkbox/single_checkbox'
    LOCATOR_CHECKBOXES = (By.LINK_TEXT, 'Checkboxes')
    LOCATOR_SUBMIT = (By.CSS_SELECTOR, 'input[type=submit]')
    LOCATOR_RESULT = (By.CLASS_NAME, 'result-text' )


    def open(self):
        self.driver.get(self.URL)


    def click_checkboxes(self):
        self.find(self.LOCATOR_CHECKBOXES).click()


    def choose_id_checkboxes(self, indexes):
        for i in indexes:
            self.wait.until(EC.element_to_be_clickable((By.ID, f'id_checkboxes_{i}'))).click()
        self.find(self.LOCATOR_SUBMIT).click()


    def result_text(self):
        self.wait.until(EC.visibility_of_element_located(self.LOCATOR_RESULT))
        return self.find(self.LOCATOR_RESULT).text
