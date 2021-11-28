from selenium.webdriver.remote.webelement import WebElement


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


class Asserter:

    @staticmethod
    def assert_element_text(button: WebElement, text):
        assert button.text == text, Asserter._err_message(text, button.text)

    @staticmethod
    def assert_language_is_selected(language_button: WebElement):
        expected_color = 'RGB(109, 73, 104)'
        color_property = language_button.value_of_css_property('background').upper()
        assert expected_color in color_property, Asserter._err_message(expected_color, color_property)

    @staticmethod
    def _err_message(expected: str, actual: str):
        return f'Expected {expected}, got {actual} instead'
