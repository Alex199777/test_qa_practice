from pages.new_tab_page import TabPage

import pytest

@pytest.mark.parametrize('link_or_button, element_id, expected',
                         [('link', 'new-page-link','I am a new page in a new tab' ),
                          ('button', 'new-page-button','I am a new page in a new tab' )
                                                        ])
def test_new_tab(driver, link_or_button, element_id, expected):
    page = TabPage(driver)
    page.open(link_or_button)
    page.click_element_by_id(element_id)
    page.switch_to_tab()
    assert page.result_text() == expected


