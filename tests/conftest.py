from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

    # browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    # yield browser
    # browser.quit()

