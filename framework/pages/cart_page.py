from enum import Enum

from .base_page import BasePage
from ..driver.locator import Locator
from ..utils import Asserter


class CartPageLocator(Locator, Enum):
    CHOOSE_PAPER_BUTTON = '//*[@id="confirm_cart"]/div[2]/div[1]/div[2]/div/div[6]/a'
    ORDER_BUTTON = '//*[@id="popupcart_extended"]/div[3]/div[2]/div/div/div[2]/button'
    PAPER_BOX = '//*[@id="confirm_cart"]/div[2]/div/div[1]/div[3]'
    NAME_INPUT = '//*[@id="input-payment-firstname"]'
    SURNAME_INPUT = '//*[@id="input-payment-lastname"]'
    PHONE_INPUT = '//*[@id="input-payment-telephone"]'
    EMAIL_INPUT = '//*[@id="input-payment-email"]'
    DELIVERY_BUTTON = '//*[@id="radio_flat"]'
    PAYMENT_BUTTON = '//*[@id="collapse-payment-method"]/div/label[1]/input'


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

    def validate_paper_choice(self):
        self._connection.wait_for_element(CartPageLocator.PAPER_BOX)

    def enter_name(self, text: str):
        self._enter_text_to_input_field(CartPageLocator.NAME_INPUT, text, "*Ім’я")

    def enter_surname(self, text: str):
        self._enter_text_to_input_field(CartPageLocator.SURNAME_INPUT, text, "*Прізвище")

    def enter_phone_number(self, text: str):
        self._enter_text_to_input_field(CartPageLocator.PHONE_INPUT, text, "*Телефон")

    def enter_email(self, text: str):
        self._enter_text_to_input_field(CartPageLocator.EMAIL_INPUT, text, "*Email")

    def _enter_text_to_input_field(self, locator: Locator, text: str, placeholder: str):
        input_field = self._connection.get_element(locator)
        Asserter.assert_input_placeholder(input_field, placeholder)
        input_field.send_keys(text)
        Asserter.assert_input(input_field, text)

    def choose_delivery_type(self):
        button = self._connection.get_element(CartPageLocator.DELIVERY_BUTTON)
        Asserter.assert_is_selected(button, is_selected=False)
        button.click()
        Asserter.assert_is_selected(button)

    def choose_payment_type(self):
        button = self._connection.get_element(CartPageLocator.PAYMENT_BUTTON)
        Asserter.assert_is_selected(button, is_selected=False)
        button.click()
        Asserter.assert_is_selected(button)