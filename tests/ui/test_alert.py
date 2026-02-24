from pages.alert_page import AlertPage


def test_alert(driver):
    obj = AlertPage(driver)
    obj.open()
    obj.click_button()
    assert obj.alert_text() == 'I am an alert!'