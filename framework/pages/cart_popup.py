from enum import Enum

from .base_page import BasePage
from ..driver.locator import Locator
from ..utils import Asserter


class CartPopupLocator(Locator, Enum):
    CONTINUE_BUTTON = '//*[@id="popupcart_extended"]/div[3]/div[2]/div/div/div[1]/button'
    ORDER_BUTTON = '//*[@id="popupcart_extended"]/div[3]/div[2]/div/div/div[2]/button'


class CartPopup(BasePage):

    def click_continue_button(self):
        locator = CartPopupLocator.CONTINUE_BUTTON
        present = self._connection.wait_for_text_in_element(locator, 'Продовжити покупки')
        if present:
            button = self._connection.get_element(locator)
            Asserter.assert_element_text(button, 'Продовжити покупки')
            button.click()
        else:
            raise Exception('Missing CONTINUE_BUTTON')

    def click_order_button(self):
        locator = CartPopupLocator.ORDER_BUTTON
        present = self._connection.wait_for_text_in_element(locator, 'Оформити замовлення')
        if present:
            button = self._connection.get_element(locator)
            Asserter.assert_element_text(button, 'Оформити замовлення')
            button.click()
        else:
            raise Exception('Missing ORDER_BUTTON')
