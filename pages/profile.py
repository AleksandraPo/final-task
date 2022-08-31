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
    patronymic = Find(by=By.ID, value="secondname")
    birth_date = Find(by=By.ID, value="birthday")
    redact = Find(
        by=By.XPATH, value='//div[@class="user-edit-block"]//a[@href="#account_redact"]'
    )
    name_area = Find(by=By.ID, value="firstname")
    profile_form = Find(by=By.ID, value="account_redact")
    save_changed_name = Find(
        by=By.XPATH, value='//input[@name="changePersonalInfo" and @type="submit"]'
    )
    check_new_name = Find(by=By.XPATH, value='//div[@class="grid_1"]//b')
