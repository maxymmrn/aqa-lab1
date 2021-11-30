from enum import Enum

from .base_page import BasePage
from ..driver.locator import Locator
from ..utils import Asserter


class CartPageLocator(Locator, Enum):
    CHOOSE_PAPER_BUTTON = '//*[@id="confirm_cart"]/div[2]/div[1]/div[2]/div/div[6]/a'
    ORDER_BUTTON = '//*[@id="popupcart_extended"]/div[3]/div[2]/div/div/div[2]/button'


class CartPage(BasePage):

    def open_paper_chooser(self):
        locator = CartPageLocator.CHOOSE_PAPER_BUTTON
        present = self._connection.wait_for_text_in_element(locator, 'Обрати папір')
        if present:
            button = self._connection.get_element(locator)
            Asserter.assert_element_text(button, 'Обрати папір')
            button.click()
        else:
            raise Exception('Missing CHOOSE_PAPER_BUTTON')
