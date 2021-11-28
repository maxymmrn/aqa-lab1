from .base_page import BasePage
from ..driver.locator import Locator
from ..utils import Asserter


class HomePage(BasePage):

    def validate_board_games_tab(self):
        tab = self._connection.wait_for_element(Locator.BOARD_GAMES_TAB)
        Asserter.assert_element_text(tab, 'Настільні ігри')

    def click_board_games_tab(self):
        self._connection.get_element(Locator.BOARD_GAMES_TAB).click()

