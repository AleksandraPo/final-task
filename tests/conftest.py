import pytest

import config
from pages.main import MainPage


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    # off loading pictures
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    return chrome_options


@pytest.fixture
def authorized_driver(selenium):
    page = MainPage(driver=selenium)
    page.open()
    page.enter.click()
    page.by_email.click()
    page.username.send_keys(config.USERNAME)
    page.password.send_keys(config.PASSWORD)
    page.login.click()
    assert page.is_element_present("profile", timeout=3)
    return selenium
