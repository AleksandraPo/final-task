from selenium.webdriver.common.action_chains import ActionChains

from pages.feedback_page import FeedBackPage


def test_send_comment(authorized_driver):
    page = FeedBackPage(authorized_driver)
    page.open()

    page.theme.click()
    ActionChains(page._driver).move_to_element(page.feedback).click(
        page.feedback
    ).perform()
    page.textarea.click()
    page.textarea.send_keys("Все супер")
    page.send.click()

    assert page.is_element_present("notification", timeout=3)
    assert "ваше сообщение отправлено." in page.notification.text.strip().lower()
