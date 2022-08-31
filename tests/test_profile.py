import random
import string

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import config
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


def test_change_name(authorized_driver):
    page = ProfilePage(authorized_driver)
    page.open()

    new_name = "".join(random.sample(string.ascii_lowercase, 5))

    page.redact.click()
    page.patronymic.clear()
    page.patronymic.send_keys(config.PATRONYMIC)
    page.name_area.clear()
    page.name_area.send_keys(new_name)
    page.name_area.click()
    page.profile_form.click()
    page.save_changed_name.click()

    WebDriverWait(page._driver, 3).until(
        EC.invisibility_of_element_located(page.profile_form)
    )
    assert new_name in page.check_new_name.text.strip().lower()
