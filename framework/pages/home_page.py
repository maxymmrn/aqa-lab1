from enum import Enum

from .base_page import BasePage
from ..driver.locator import Locator
from ..utils import Asserter


class HomePageLocator(Locator, Enum):
    BOARD_GAMES_TAB = '//*[@id="menu"]/div[2]/ul/li[1]/a'


class HomePage(BasePage):

    def click_board_games_tab(self):
        tab = self._connection.wait_for_element(HomePageLocator.BOARD_GAMES_TAB)
        Asserter.assert_element_text(tab, 'Настільні ігри')
        tab.click()

