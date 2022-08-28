from dataclasses import asdict

from webium import BasePage, Find

from .locators import AuthLocators


class AuthPage(BasePage):
    url = "https://www.traektoria.ru/"

    enter = Find(**asdict(AuthLocators.enter))
    by_email = Find(**asdict(AuthLocators.by_email))
    username = Find(**asdict(AuthLocators.username))
    password = Find(**asdict(AuthLocators.password))
    login = Find(**asdict(AuthLocators.login))
    name = Find(**asdict(AuthLocators.name))

