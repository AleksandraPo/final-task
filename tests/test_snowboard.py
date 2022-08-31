import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.basket import BasketPage
from pages.product import ProductPage
from pages.snowboards import SnowboardsPage


def test_basket_with_item(selenium):
    page = SnowboardsPage(selenium)
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
    page = SnowboardsPage(selenium)
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
    page = SnowboardsPage(authorized_driver)
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
    page = SnowboardsPage(selenium)
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


@pytest.mark.parametrize(
    "code, url",
    (
        ("GENDER_PUB", "/gender-man"),
        ("SIZE", "SIZE="),
        ("THING_TYPE", "THING_TYPE="),
        ("CML2_MANUFACTURER", "/brand"),
        ("TECHNOLOGIES", "TECHNOLOGIES="),
        ("SKU_COLOR_FOR_FILTER", "SKU_COLOR_FOR_FILTER="),
        ("FLEX", "FLEX="),
        ("LEVEL", "LEVEL="),
        ("SHAPE", "SHAPE="),
        ("RIDING_STYLE", "RIDING_STYLE="),
        ("BEND", "BEND="),
        ("SHOPS", "shops="),
    ),
)
def test_filter_for_products(selenium, code, url):
    page = SnowboardsPage(selenium)
    page.open()

    _filter = page.get_filter(code)
    _filter.click()
    _filter.items[0].click()
    WebDriverWait(page._driver, 10).until(
        EC.invisibility_of_element_located(page.preloader)
    )
    assert url in page._driver.current_url


@pytest.mark.parametrize(
    "code, domain",
    (
        ("vk", "vk.com"),
        ("ok", "ok.ru"),
        ("go", "google.com"),
        ("pi", "pinterest.com"),
    ),
)
def test_share_with_friends(selenium, code, domain):
    page = SnowboardsPage(selenium)
    page.open()
    assert page.items, "Items not found"

    url = page.items[0].p_link.get_attribute("href")
    item_page = ProductPage(selenium, url)
    item_page.open()

    social = item_page.get_social(code)
    WebDriverWait(item_page._driver, 5).until(
        EC.visibility_of_element_located((social.by, social.value))
    )
    social.click()
    window_after = item_page._driver.window_handles[1]
    item_page._driver.switch_to_window(window_after)
    assert domain in item_page._driver.current_url
