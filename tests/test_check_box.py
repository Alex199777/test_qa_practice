from pages.checkbox_page import CheckboxPage

import pytest

@pytest.mark.parametrize('indexes, expected', [([0, 2], 'one, three'),
                                               ([1], 'two')
                                               ])
def test_checkboxes(driver, indexes, expected):
    checkbox = CheckboxPage(driver)
    checkbox.open()
    checkbox.click_checkboxes()
    checkbox.choose_id_checkboxes(indexes)
    assert checkbox.result_text() == expected


    # driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    # driver.find_element(By.LINK_TEXT, 'Checkboxes').click()
    # for i in indexes:
    #     checkbox = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, f'id_checkboxes_{i}')))
    #     checkbox.click()
    # driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()
    # result = driver.find_element(By.CLASS_NAME, 'result-text' ).text
    # assert result == expected




