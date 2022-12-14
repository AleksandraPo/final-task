from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from webium import BasePage, Find

import config


class FeedBackPage(BasePage):
    url = urljoin(config.ROOT_URL, "/help/feedback/")

    # locators
    theme = Find(
        by=By.XPATH,
        value='//div[@class = "ik_select_link_text" and '
        'contains(text(),"Выберите тему")]',
    )
    feedback = Find(
        by=By.XPATH,
        value='//div[@id="mCSB_2"]'
        '//li/span[contains(text(),"Оставить отзыв о компании")]',
    )
    textarea = Find(by=By.ID, value="feedback_MESSAGE")
    send = Find(by=By.XPATH, value='//form[@id="feedback_form"]//input[@type="submit"]')
    notification = Find(
        by=By.XPATH, value='//div[@id="support_form_block"]//div[@class="notification"]'
    )
