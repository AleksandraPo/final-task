import time

from selenium.webdriver import ActionChains

import config
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


def test_profile_page(authorized_driver):
    page = ProfilePage(authorized_driver)
    page.open()

    assert page.is_element_present("title", timeout=3)
    assert page.title.text.strip().lower() == "личный кабинет"


def test_profile_page_not_auth(selenium):
    page = ProfilePage(selenium)
    page.open()

    assert page.is_element_present("enter", timeout=3)
    header = page.enter.find_element_by_xpath("./h1")
    assert header.text.strip().lower() == "вход на сайт"
