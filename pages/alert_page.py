from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class AlertPage(BasePage):
    URL = 'https://www.qa-practice.com/elements/alert/alert'
    LOCATOR_BUTTON = (By.CSS_SELECTOR, '.a-button')

    def open(self):
        self.driver.get(self.URL)

    def click_button(self):
        self.find(self.LOCATOR_BUTTON).click()

    def alert_text(self):
        return self.wait.until(EC.alert_is_present()).text

