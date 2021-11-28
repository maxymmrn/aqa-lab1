from ..driver.connection import Connection, Locator
from ..utils import Asserter


class BasePage:

    def __init__(self, connection: Connection):
        self._connection = connection

    def validate_language(self):
        ua_lang = self._connection.wait_for_element(Locator.UA_LANGUAGE_BUTTON)
        Asserter.assert_language_is_selected(ua_lang)

