from selenium.webdriver import ActionChains

import config
from pages.main_page import MainPage


def test_auth_page(authorized_driver):
    page = MainPage(authorized_driver)
    page.open()

    assert page.profile.text.strip().lower() == "skill factory"


def test_hover_profile_menu(authorized_driver):
    page = MainPage(authorized_driver)
    page.open()

    assert not page.is_element_present("profile_menu", timeout=3)

    actions = ActionChains(page._driver)
    actions.move_to_element(page.profile)
    actions.perform()

    assert page.is_element_present("profile_menu")


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


def test_auth_page_wrong_password_actions(selenium):
    page = MainPage(selenium)
    page.open()
    actions = ActionChains(page._driver)
    actions.click(page.enter)
    actions.click(page.by_email)
    actions.send_keys_to_element(page.username, config.USERNAME)
    actions.send_keys_to_element(page.password, config.PASSWORD + "a")
    actions.click(page.login)
    actions.perform()

    assert page.is_element_present("auth_error", timeout=3)


def test_tg_link_works(selenium):
    page = MainPage(selenium)
    page.open()
    assert page.telegram.get_attribute("href") == "https://t.me/traektoria_boardshop"


def test_vk_link_works(selenium):
    page = MainPage(selenium)
    page.open()
    assert page.vk.get_attribute("href") == "https://vk.com/traektoriaboardshop"


def test_youtube_link_works(selenium):
    page = MainPage(selenium)
    page.open()
    assert (
        page.youtube.get_attribute("href")
        == "https://www.youtube.com/channel/UC05By8FMmQHacyDQG5Vzehw?sub_confirmation=1"
    )


def test_menu(selenium):
    page = MainPage(selenium)
    page.open()
    page.btn_menu.click()
    assert page.is_element_present("menu", timeout=3)
