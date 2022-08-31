import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import config
from pages.main_page import MainPage


def test_auth_page(authorized_driver):
    page = MainPage(authorized_driver)
    page.open()

    WebDriverWait(page._driver, 3).until(EC.invisibility_of_element_located(page.lk))
    assert not page.is_element_present("lk", just_in_dom=True)


def test_hover_profile_menu(authorized_driver):
    page = MainPage(authorized_driver)
    page.open()

    assert not page.is_element_present("profile_menu", timeout=3)

    actions = ActionChains(page._driver)
    actions.move_to_element(page.profile)
    actions.perform()

    assert page.is_element_present("profile_menu")


def test_auth_page_actions(selenium):
    page = MainPage(selenium)
    page.open()
    actions = ActionChains(page._driver)
    actions.click(page.enter)
    actions.click(page.by_email)
    actions.send_keys_to_element(page.username, config.USERNAME)
    actions.send_keys_to_element(page.password, config.PASSWORD)
    actions.click(page.login)
    actions.perform()

    WebDriverWait(page._driver, 3).until(EC.invisibility_of_element_located(page.lk))
    assert not page.is_element_present("lk", just_in_dom=True)


def test_auth_page_actions_by_phone(selenium):
    page = MainPage(selenium)
    page.open()

    page.enter.click()
    page.phone_input.click()
    page.phone_input.send_keys(config.PHONE)
    page.enter_by_phone.click()

    assert page.is_element_present("sent_code", timeout=3)


def test_auth_page_actions_with_wrong_password(selenium):
    page = MainPage(selenium)
    page.open()
    actions = ActionChains(page._driver)
    actions.click(page.enter)
    actions.click(page.by_email)
    actions.send_keys_to_element(page.username, config.USERNAME)
    actions.send_keys_to_element(page.password, config.PASSWORD + "a")
    actions.click(page.login)
    actions.perform()

    assert page.is_element_present("auth_error", timeout=3)


def test_tg_link_works(selenium):
    page = MainPage(selenium)
    page.open()
    assert page.telegram.get_attribute("href") == "https://t.me/traektoria_boardshop"


def test_vk_link_works(selenium):
    page = MainPage(selenium)
    page.open()
    assert page.vk.get_attribute("href") == "https://vk.com/traektoriaboardshop"


def test_youtube_link_works(selenium):
    page = MainPage(selenium)
    page.open()
    assert (
        page.youtube.get_attribute("href")
        == "https://www.youtube.com/channel/UC05By8FMmQHacyDQG5Vzehw?sub_confirmation=1"
    )


def test_menu(selenium):
    page = MainPage(selenium)
    page.open()
    page.btn_menu.click()
    assert page.is_element_present("menu", timeout=3)


def test_recall_me(selenium):
    page = MainPage(selenium)
    page.open()
    page.btn_recall.click()
    assert page.is_element_present("number_form", timeout=3)


@pytest.mark.parametrize(
    "code, city",
    (
        ("1", "москва"),
        ("2", "санкт-петербург"),
        ("4", "другой город"),
        ("5", "беларусь"),
        ("6", "казахстан"),
        ("7", "другой регион"),
        ("8", "сочи"),
        ("9", "екатеринбург"),
    ),
)
def test_change_city(selenium, code, city):
    page = MainPage(selenium)
    page.open()

    page.other_region.click()
    page.get_city(code).click()
    WebDriverWait(page._driver, 3).until(
        EC.invisibility_of_element_located(page.preloader)
    )
    assert city in page.city.text.strip().lower()


@pytest.mark.parametrize(
    "link",
    (
        "/traektoriya-na-paveletskoy",
        "/traektoriya-stok",
        "/traektoria-tts-aviapark",
        "/b-shop",
        "/surf-style",
        "/peak",
    ),
)
def test_shop_links(selenium, link):
    page = MainPage(selenium)
    page.open()

    links = {s.get_attribute("href") for s in page.shops}
    assert len(links) == 6
    assert any(link in l for l in links)
