from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from .base_page import BasePage

class TabPage(BasePage):

    URL = 'https://www.qa-practice.com/elements/new_tab/'
    LOCATOR_RESULT = (By.CLASS_NAME, 'result-text')


    def open(self, link_or_button):
        self.driver.get(self.URL + link_or_button)


    def click_element_by_id(self, element_id):
        element = (By.ID, element_id)
        self.find(element).click()

    def switch_to_tab(self):
        tab = self.driver.window_handles
        self.driver.switch_to.window(tab[1])

    def result_text(self):
        self.wait.until(EC.visibility_of_element_located(self.LOCATOR_RESULT))
        return self.find(self.LOCATOR_RESULT).text
