# Final task. "[Traektoria.ru](https://www.traektoria.ru/)" shop
### Run tests
Before run tests
```
pip install -r requirements.txt
```

Run tests with Chrome driver
```
pytest --driver Chrome --driver-path /path/to/chromedriver tests
```

To specify your driver see [docs](https://pytest-selenium.readthedocs.io/en/latest/user_guide.html#specifying-a-browser).

### Description
Протестированы страницы: 

    - главная (авторизация, возможность выбора города, ссылки на соцсети, меню )
    - профиль (изменение личных данных, отправка сообщения)
    - корзина (удаление товаров из корзины)
    - магазины (наличие магазинов в разных городах, отображение на карте точек магазинов)
    - сноуборды (фильтры, добавление в избранное, добавление в корзину, поделиться с друзьями)