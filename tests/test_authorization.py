from selenium.webdriver import ActionChains

import config
from pages.main_page import MainPage


def test_auth_page(authorized_driver):
    page = MainPage(authorized_driver)
    page.open()

    assert page.is_element_present("profile", timeout=3)
    assert page.profile.text.strip().lower() == "skill factory"


def test_auth_page_actions(selenium):
    page = MainPage(selenium)
    page.open()
    actions = ActionChains(page._driver)
    actions.click(page.enter)
    actions.click(page.by_email)
    actions.send_keys_to_element(page.username, config.USERNAME)
    actions.send_keys_to_element(page.password, config.PASSWORD)
    actions.click(page.login)
    actions.perform()

    assert page.is_element_present("profile", timeout=3)
    assert page.profile.text.strip().lower() == "skill factory"
