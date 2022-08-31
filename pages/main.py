from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds

import config


class MainPage(BasePage):
    url = config.ROOT_URL

    # locators
    enter = Find(by=By.XPATH, value='//span[@class="trigger"]')
    by_email = Find(by=By.XPATH, value='//a[text()="Войти по почте"]')
    phone_input = Find(
        by=By.XPATH, value='//input[contains(concat(" ", @class, " "), " phone_mask ")]'
    )
    sent_code = Find(
        by=By.XPATH, value='//div[@class="form-wrapper__row js-insert-inputs"]'
    )
    enter_by_phone = Find(
        by=By.XPATH, value='//div[@class="form-wrapper__row js-insert-repeatCode"]//div'
    )
    profile = Find(
        by=By.XPATH, value='//div[contains(concat(" ", @class, " "), " user_login ")]/a'
    )
    profile_menu = Find(
        by=By.XPATH,
        value='//div[contains(concat(" ", @class, " "), " user_login ")]'
        '//ul[@class="submenu"]',
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
        value='//div[@class="sub"]//div[@class="sub_content"]'
        '//div[@class="columns clearfix"]//ul[@class="submenu"]',
    )
    auth_error = Find(
        by=By.XPATH, value='//div[contains(text(),"Неверный логин или пароль.")]'
    )
    btn_recall = Find(by=By.ID, value="comp_f8cc4e9a81735f1089a1fd6d93b0c3ce")
    number_form = Find(by=By.ID, value="callback")

    shops = Finds(by=By.XPATH, value='//div[@class="shops"]//div[@class="sub"]//li//a')
    city = Find(by=By.XPATH, value='//span[@class="trigger kinda_select"]')
    other_region = Find(
        by=By.XPATH, value='//a[@class="trigger_show_other gray_link fs13"]'
    )
    preloader = Find(by=By.ID, value="preloader")
    lk = Find(by=By.ID, value="authAppMini")

    def get_city(self, code):
        return Find(
            by=By.XPATH,
            value=f'//div[contains(concat(" ", @class, " "), " show_other ")]//'
            f'a[contains(concat(" ", @class, " "), " set_region ") and '
            f'@data-region-id="{code}"]',
            context=self,
        )
