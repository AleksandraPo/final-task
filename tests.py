import pytest

import config
from pages.auth_page import AuthPage


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    return chrome_options


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.open()
    page.enter.click()
    page.by_email.click()
    page.username.send_keys(config.USERNAME)
    page.password.send_keys(config.PASSWORD)
    page.login.click()

    assert page.is_element_present("name", timeout=3)
    assert page.name.text.strip().lower() == "skill factory"