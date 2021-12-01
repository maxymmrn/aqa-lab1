from enum import Enum

from .base_page import BasePage
from ..driver.locator import Locator
from ..utils import Asserter


class PaperChooserPopupLocator(Locator, Enum):
    PAPER_OPTION = '//*[@id="input-option562"]/div[WILDCARD]/label/span'
    CONFIRM_BUTTON = '//*[@id="modalChoose247"]/div/div/div/div[5]/button[2]'


class PaperChooserPopup(BasePage):

    def choose_paper(self, number: int):
        locator = PaperChooserPopupLocator.PAPER_OPTION.replace('WILDCARD', str(number))
        self._connection.wait_for_element(locator).click()

    def confirm(self):
        locator = PaperChooserPopupLocator.CONFIRM_BUTTON
        present = self._connection.wait_for_text_in_element(locator, 'Обрати')
        if present:
            button = self._connection.get_element(locator)
            Asserter.assert_element_text(button, 'Обрати')
            button.click()
        else:
            raise Exception('Missing CONFIRM_BUTTON')
