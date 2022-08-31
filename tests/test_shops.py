import time

import pytest

from pages.shop import ShopsPage, ShopPage


@pytest.mark.parametrize(
    "city,shop_count",
    (
        ("moscow", 6),
        ("ekb", 1),
        ("sochi", 1),
        ("petersburg", 2),
    ),
)
def test_city_shops(selenium, city, shop_count):
    page = ShopPage(code=city, driver=selenium)
    page.open()

    assert len(list(page.shops)) == shop_count


@pytest.mark.parametrize(
    "city,shop_count",
    (
        ("moscow", 6),
        ("ekb", 1),
        ("sochi", 1),
        ("petersburg", 2),
    ),
)
def test_city_shops_on_map(selenium, city, shop_count):
    page = ShopPage(code=city, driver=selenium)
    page.open()

    time.sleep(5)
    count = 0
    points = page.ymaps.points
    for point in points:
        if point.text:
            count += int(point.text)
        else:
            count += 1

    assert count == shop_count


@pytest.mark.parametrize(
    "city",
    ("moscow", "ekb", "sochi", "petersburg"),
)
def test_shops_cities(selenium, city):
    page = ShopsPage(selenium)
    page.open()

    links = {c.get_attribute("href") for c in page.cities}
    assert len(links) == 4
    assert any(city in l for l in links)
