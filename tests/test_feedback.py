import time

from selenium.webdriver import ActionChains

import config
from pages.feedback_page import FeedBackPage


# E       selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//form[@id="feedback_form"]//li[contains(text(),"Оставить отзыв о компании")]"}


def test_send_comment(authorized_driver):
    page = FeedBackPage(authorized_driver)
    page.open()

    actions = ActionChains(page._driver)
    actions.click(page.theme)
    actions.click(page.feedback)
    actions.click(page.textarea)
    actions.send_keys_to_element(page.textarea, "Все супер")
    actions.click(page.send)
    actions.perform()

    assert page.is_element_present("notification", timeout=3)
    assert "ваше сообщение отправлено." in page.notification.text.strip().lower()
