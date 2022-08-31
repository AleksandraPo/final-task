from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find, Finds

import config


class Item(WebElement):
    buy = Find(
        by=By.XPATH, value='.//a[contains(concat(" ", @class, " "), " button-buy ")]'
    )
    add = Find(
        by=By.XPATH,
        value='.//div[contains(concat(" ", @class, " "), " kdxAddToCart ")]',
    )
    image = Find(
        by=By.XPATH, value='.//div[contains(concat(" ", @class, " "), " p_main_img ")]'
    )
    p_link = Find(by=By.XPATH, value='.//a[@class="p_link"]')


class Filter(WebElement):
    items = Finds(by=By.XPATH, value=".//li")


class SnowboardsPage(BasePage):
    url = urljoin(config.ROOT_URL, "/snowboard/boards/")

    # locators
    items = Finds(
        Item,
        by=By.XPATH,
        value='//div[@id="catalog_container"]/div[@itemprop="itemListElement"]',
    )
    basket = Find(by=By.XPATH, value='//div[@id="cartSmall"]//a')
    preloader = Find(by=By.ID, value="preloader")

    filter_gender = Find(by=By.XPATH, value='//div[@data-property_code="GENDER_PUB"]')
    filter_size = Find(by=By.XPATH, value='//div[@data-property_code="SIZE"]')
    menu_gender = Find(by=By.XPATH, value='//ul[@data-property_code="GENDER_PUB"]')
    btn_men = Find(by=By.XPATH, value='//ul[@data-property_code="GENDER_PUB"]/li[1]')

    def get_filter(self, code: str):
        return Find(
            Filter,
            by=By.XPATH,
            value=f'//div[@data-property_code="{code}"]',
            context=self,
        )
