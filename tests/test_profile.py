from selenium.webdriver import ActionChains

from pages.main_page import MainPage


def test_hover_profile_menu(authorized_driver):
    page = MainPage(authorized_driver)
    page.open()

    assert not page.is_element_present("profile_menu", timeout=3)

    actions = ActionChains(page._driver)
    actions.move_to_element(page.profile)
    actions.perform()

    assert page.is_element_present("profile_menu")
