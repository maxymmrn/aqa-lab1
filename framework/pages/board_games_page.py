from enum import Enum
from time import sleep
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from ..driver.locator import Locator
from ..utils import Asserter


class BoardGamesPageLocator(Locator, Enum):
    FILTER_SECTION = '//*[@id="rdrf36"]'
    MONEY_FILTER = '//*[@id="rdrf36-price-group"]/div/span/span[6]'
    PLAYERS_NUMBER_FILTER = '//*[@id="rdrf36-attr15-group"]/div/span/span[7]'
    UA_LANGUAGE_FILTER = '//*[@id="rdrf36-attr16-5269f4d75f5bc75f0f94bab2100a5531"]/label'
    ACCEPT_FILTER_BUTTON = '//*[@id="rdrf-form36"]/div[2]/button[2]'
    PRICE_LABEL = '//*[@id="rdrf36-price-group"]/div/span/span[1]/span[4]'
    PLAYERS_NUMBER_LABEL = '//*[@id="rdrf36-attr15-group"]/div/span/span[1]/span[5]'
    BUY_BUTTON = '//*[@id="content"]/div[3]/div[WILDCARD]/div/div[2]/button'
    CART_BUTTON = '//*[@id="cart"]/button'


class BoardGamesPage(BasePage):

    def validate_filter_is_present(self):
        self._connection.wait_for_element(BoardGamesPageLocator.FILTER_SECTION)

    def move_price_filter(self, dx: int):
        before_price = self.get_price_from_filter().text
        self._connection.move_element_by_offset(BoardGamesPageLocator.MONEY_FILTER, dx=dx)
        after_price = self.get_price_from_filter().text
        Asserter.assert_label_changed(before_price, after_price)

    def get_price_from_filter(self) -> WebElement:
        return self._connection.get_element(BoardGamesPageLocator.PRICE_LABEL)

    def get_players_number_from_filter(self) -> WebElement:
        return self._connection.get_element(BoardGamesPageLocator.PLAYERS_NUMBER_LABEL)

    def buy_buttons(self) -> List[WebElement]:
        for i in range(1, 7):
            locator = BoardGamesPageLocator.BUY_BUTTON.replace('WILDCARD', str(i))
            button = self._connection.wait_for_element(locator)
            yield button
            previous_button = self._connection.wait_for_element(locator)
            Asserter.assert_element_text_one_of(previous_button, ['Купити', 'Передзамовити'])

    def move_players_number_filter(self, dx: int):
        before_number = self.get_players_number_from_filter().text
        self._connection.move_element_by_offset(BoardGamesPageLocator.PLAYERS_NUMBER_FILTER, dx=dx)
        after_number = self.get_players_number_from_filter().text
        Asserter.assert_label_changed(before_number, after_number)

    def choose_ua_games(self):
        self._connection.get_element(BoardGamesPageLocator.UA_LANGUAGE_FILTER).click()

    def accept_filter(self):
        button = self._connection.get_element(BoardGamesPageLocator.ACCEPT_FILTER_BUTTON)
        Asserter.assert_element_text(button, 'Застосувати')
        button.click()

    def click_cart_button(self):
        self._connection.get_element(BoardGamesPageLocator.CART_BUTTON).click()

