from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pytest

from pages.select_page import SelectPage


@pytest.mark.parametrize('place, transport, when_time, expected',
                         [('Sea', 'Air', 'Tomorrow', 'to go by air to the sea tomorrow'),
                          ('Ocean', 'Bus', 'Today', 'to go by bus to the ocean today'),
                          ('Mountains', 'Car', 'Next week', 'to go by car to the mountains next week')])
def test_selected(driver, place, transport, when_time, expected):
    select_obj = SelectPage(driver)
    select_obj.open()
    select_obj.fill_form(place, transport, when_time)
    select_obj.click_submit()
    assert select_obj.result(expected) == expected



    # driver.get('https://www.qa-practice.com/elements/select/single_select')
    # driver.find_element(By.LINK_TEXT, 'Multiple selects').click()
    # Select(driver.find_element(By.CSS_SELECTOR,
    #                            'select[name=choose_the_place_you_want_to_go]')).select_by_visible_text(place)
    # Select(driver.find_element(By.CSS_SELECTOR,
    #                            'select[name=choose_how_you_want_to_get_there]')).select_by_visible_text(transport)
    # Select(driver.find_element(By.CSS_SELECTOR,
    #                            'select[name=choose_when_you_want_to_go]')).select_by_visible_text(when_time)
    #
    # driver.find_element(By.ID, 'submit-id-submit').click()
    # result = driver.find_element(By.CLASS_NAME, 'result-text').text
    # assert result == expected



