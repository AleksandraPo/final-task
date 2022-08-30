import time

from selenium.webdriver import ActionChains

from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.snowboards_page import SnowboardPage


def test_basket_with_item(selenium):
    page = SnowboardPage(selenium)
    page.open()
    assert page.items, "Items not found"

    item = page.items[0]
    ActionChains(page._driver).move_to_element(item).click(item.buy).perform()
    time.sleep(3)
    ActionChains(page._driver).move_to_element(item.add).click(item.add).perform()

    assert page.is_element_present("basket", timeout=3)
    time.sleep(2)
    assert "1 товар" in page.basket.text.strip().lower()


def test_add_item_to_wishList(selenium):
    page = SnowboardPage(selenium)
    page.open()
    assert page.items, "Items not found"

    url = page.items[0].p_link.get_attribute("href")
    item_page = ProductPage(selenium, url)
    item_page.open()

    assert item_page.is_element_present("wishlist_button", timeout=3)
    item_page.wishlist_button.click()
    assert item_page.is_element_present("wishlist", timeout=3)
    time.sleep(2)
    assert "0" in item_page.wishlist.text.strip().lower()


def test_add_item_to_wishList_authorizated(authorized_driver):
    page = SnowboardPage(authorized_driver)
    page.open()
    assert page.items, "Items not found"

    url = page.items[0].p_link.get_attribute("href")
    item_page = ProductPage(authorized_driver, url)
    item_page.open()

    assert item_page.is_element_present("wishlist_button", timeout=3)
    item_page.wishlist_button.click()
    assert item_page.is_element_present("wishlist", timeout=3)
    time.sleep(2)
    assert "1" in item_page.wishlist.text.strip().lower()


def test_delete_item_from_basket(selenium):
    page = SnowboardPage(selenium)
    page.open()
    assert page.items, "Items not found"

    item = page.items[0]
    ActionChains(page._driver).move_to_element(item).click(item.buy).perform()
    time.sleep(3)
    ActionChains(page._driver).move_to_element(item.add).click(item.add).perform()

    assert page.is_element_present("basket", timeout=3)
    time.sleep(2)
    assert "1 товар" in page.basket.text.strip().lower()

    # url = page.items[0].p_link.get_attribute('href')
    basket = BasketPage(selenium)
    basket.open()
    basket.delete_button.click()
    basket.accept_delete.click()
    assert "в вашей корзине нет товаров" in basket.clear_basket.text.strip().lower()
