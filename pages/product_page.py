from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find, Finds
from urllib.parse import urljoin

import config


class ProductPage(BasePage):

    # locators
    wishlist_button = Find(
        by=By.XPATH,
        value='//div[contains(concat(" ", @class, " "), " to_favourites ")]',
    )
    wishlist = Find(by=By.ID, value="wishList")
