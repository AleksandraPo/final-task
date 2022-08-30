from selenium.webdriver.common.by import By
from webium import BasePage, Find


class ProductPage(BasePage):

    # locators
    wishlist_button = Find(
        by=By.XPATH,
        value='//div[contains(concat(" ", @class, " "), " to_favourites ")]',
    )
    wishlist = Find(by=By.ID, value="wishList")
