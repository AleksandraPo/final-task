from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find, Finds
from urllib.parse import urljoin

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
    p_link = Find(by=By.XPATH, value='//a[@class="p_link"]')


class SnowboardPage(BasePage):
    url = urljoin(config.ROOT_URL, "/snowboard/boards/gender-man/")

    # locators
    items = Finds(
        Item,
        by=By.XPATH,
        value='//div[@id="catalog_container"]/div[@itemprop="itemListElement"]',
    )
    basket = Find(by=By.XPATH, value='//div[@id="cartSmall"]//a')
