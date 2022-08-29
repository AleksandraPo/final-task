from selenium.webdriver.common.by import By
from webium import BasePage, Find

import config


class MainPage(BasePage):
    url = config.ROOT_URL

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
    telegram = Find(
        by=By.XPATH, value='//a[@class="footer-social__item footer-social__telegramm"]'
    )
    vk = Find(by=By.XPATH, value='//a[@class="footer-social__item footer-social__vk"]')
    youtube = Find(
        by=By.XPATH, value='//a[@class="footer-social__item footer-social__youtube"]'
    )
    btn_menu = Find(by=By.XPATH, value='//li[@class="toplvl hassub first_menu"]')
    menu = Find(
        by=By.XPATH,
        value='//div[@class="sub"]//div[@class="sub_content"]//div[@class="columns clearfix"]//ul[@class="submenu"]',
    )
    auth_error = Find(
        by=By.XPATH, value='//div[contains(text(),"Неверный логин или пароль.")]'
    )
