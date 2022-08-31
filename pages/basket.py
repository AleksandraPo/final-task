from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from webium import BasePage, Find

import config


class BasketPage(BasePage):
    url = urljoin(config.ROOT_URL, "/cart/")

    # locators
    delete_button = Find(by=By.XPATH, value='//a[@class="clear_cart_button"]')
    accept_delete = Find(
        by=By.XPATH,
        value='//div[@class="trk-modal"]'
        '//div[contains(concat(" ", @class, " "), " button ")]'
        '/span[contains(text(),"Ок")]/parent::div',
    )
    clear_basket = Find(by=By.XPATH, value='//div[@class="central_text"]')
