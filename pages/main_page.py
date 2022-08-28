from selenium.webdriver.common.by import By
from webium import BasePage, Find


class MainPage(BasePage):
    url = "https://www.traektoria.ru/"

    # locators
    enter = Find(by=By.XPATH, value='//span[@class="trigger"]')
    by_email = Find(by=By.XPATH, value='//a[text()="Войти по почте"]')
    profile = Find(
        by=By.XPATH, value='//div[contains(concat(" ", @class, " "), " user_login ")]/a'
    )
    profile_menu = Find(
        by=By.XPATH,
        value='//div[contains(concat(" ", @class, " "), " user_login ")]//ul[@class="submenu"]',
    )
    login = Find(by=By.XPATH, value='//input[@type="submit" and @value="Войти"]')
    username = Find(by=By.XPATH, value='//input[@data-target="USER_LOGIN"]')
    password = Find(by=By.XPATH, value='//input[@data-target="USER_PASSWORD"]')
