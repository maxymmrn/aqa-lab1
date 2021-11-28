from .base_page import BasePage
from ..driver.locator import Locator
from ..utils import Asserter


class BoardGamesPage(BasePage):

    def validate_filter_is_present(self):
        self._connection.wait_for_element(Locator.FILTER_SECTION)

    def move_price_filter(self, dx: int):
        self._connection.move_element_by_offset(Locator.MONEY_FILTER, dx=dx)

    def move_players_number_filter(self, dx: int):
        self._connection.move_element_by_offset(Locator.PLAYERS_NUMBER_FILTER, dx=dx)

    def choose_ua_games(self):
        self._connection.get_element(Locator.UA_LANGUAGE_FILTER).click()

    def accept_filter(self):
        self._connection.get_element(Locator.ACCEPT_FILTER_BUTTON).click()

