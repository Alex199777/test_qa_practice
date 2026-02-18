from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

