from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from webium import BasePage, Find

import config


class ProfilePage(BasePage):
    url = urljoin(config.ROOT_URL, "/personal/")

    # locators
    title = Find(by=By.ID, value="pagetitle")
    enter = Find(by=By.ID, value="authApp")

    by_email = Find(by=By.XPATH, value='//a[text()="Войти по почте"]')
    profile = Find(
        by=By.XPATH, value='//div[contains(concat(" ", @class, " "), " user_login ")]/a'
    )
