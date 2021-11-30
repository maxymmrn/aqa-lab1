from enum import Enum

from ..driver.connection import Connection, Locator
from ..utils import Asserter


class BasePageLocator(Locator, Enum):
    UA_LANGUAGE_BUTTON = '//*[@id="form-language"]/ul/li[1]/a'


class BasePage:

    def __init__(self, connection: Connection):
        self._connection = connection

    def validate_language(self):
        ua_lang = self._connection.wait_for_element(BasePageLocator.UA_LANGUAGE_BUTTON)
        Asserter.assert_language_is_selected(ua_lang)

