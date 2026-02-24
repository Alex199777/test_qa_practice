from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

    # browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    # yield browser
    # browser.quit()

@pytest.fixture()
def base_url():
    def add_endpoint(endpoint):
        return f'https://dog.ceo/api/{endpoint}'
    return add_endpoint