from selenium import webdriver
from enum import Enum, auto


class Browser(Enum):
    CHROME = auto()
    FIREFOX = auto()


class DriverFactory:

    @staticmethod
    def get_driver(browser: Browser) -> webdriver:
        if browser == Browser.CHROME:
            return webdriver.Chrome()
        elif browser == Browser.FIREFOX:
            return webdriver.Firefox()
