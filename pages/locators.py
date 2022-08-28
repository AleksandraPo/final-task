from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class Locator:
    by: str = None
    value: str = None


class AuthLocators:
    enter = Locator(by=By.XPATH, value='//span[@class="trigger"]')
    by_email = Locator(by=By.XPATH, value='//a[text()="Войти по почте"]')
    name = Locator(
        by=By.XPATH, value='//div[contains(concat(" ", @class, " "), " user_login ")]/a'
    )
    login = Locator(by=By.XPATH, value='//input[@type="submit" and @value="Войти"]')
    username = Locator(by=By.XPATH, value='//input[@data-target="USER_LOGIN"]')
    password = Locator(by=By.XPATH, value='//input[@data-target="USER_PASSWORD"]')
