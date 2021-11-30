from typing import List

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from .driver_factory import DriverFactory, Browser
from .locator import Locator
from ..utils import singleton


@singleton
class Connection:

    def __init__(self, browser: Browser = Browser.CHROME):
        self._driver = DriverFactory.get_driver(browser)
        self._set_up()

    def _set_up(self):
        self._driver.get('https://octopus.in.ua/')
        self._driver.implicitly_wait(5)
        self._driver.set_window_size(1920, 1080)

    def get_element(self, locator: Locator) -> WebElement:
        return self._driver.find_element_by_xpath(locator)

    def wait_for_element(self, locator: Locator, timeout: int = 5) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(ec.presence_of_element_located((By.XPATH, locator)))

    def wait_for_text_in_element(self, locator: Locator, text: str, timeout: int = 5) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(ec.text_to_be_present_in_element((By.XPATH, locator), text))

    def wait_for_elements(self, locator: Locator, timeout: int = 5) -> List[WebElement]:
        return WebDriverWait(self._driver, timeout).until(ec.presence_of_all_elements_located((By.XPATH, locator)))

    def move_element_by_offset(self, locator: Locator, dx: int = 0, dy: int = 0):
        element = self.get_element(locator)
        ActionChains(self._driver)\
            .move_to_element(element)\
            .click_and_hold()\
            .move_by_offset(xoffset=dx, yoffset=dy)\
            .release()\
            .perform()

    def kill_session(self):
        self._driver.quit()
