from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find, Finds

import config


class Ymaps(WebElement):
    points = Finds(by=By.XPATH, value='.//ymaps[contains(@class, "places-pane")]/ymaps')


class ShopPage(BasePage):
    ymaps = Find(Ymaps, by=By.ID, value="map-canvas")

    def __init__(self, code, driver=None):
        self.shops = Finds(by=By.XPATH, value=f'//div[@id="{code}"]//div', context=self)

        url = urljoin(urljoin(config.ROOT_URL, "/about/shops/"), code)
        super(ShopPage, self).__init__(driver, url)


class ShopsPage(BasePage):
    url = urljoin(config.ROOT_URL, "/about/shops/")

    # locators
    cities = Finds(
        by=By.XPATH,
        value='//div[contains(concat(" ", @class, " "), " region_menu ")]//li//a',
    )
