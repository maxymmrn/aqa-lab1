from typing import List

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
    def assert_label_changed(before: str, after: str):
        assert before != after, f"Label didn't changed: {before} == {after}"

    @staticmethod
    def assert_elements_number(elements: List[WebElement], min_length: int):
        actual_length = len(elements)
        assert actual_length >= min_length, Asserter._err_message(min_length, actual_length)

    @staticmethod
    def assert_input_placeholder(input_field: WebElement, expected_placeholder: str):
        actual_text = input_field.get_attribute('placeholder')
        assert actual_text == expected_placeholder, Asserter._err_message(expected_placeholder, actual_text)

    @staticmethod
    def assert_input(input_field: WebElement, expected_text: str):
        actual_text = input_field.get_attribute('value')
        assert actual_text == expected_text, Asserter._err_message(expected_text, actual_text)

    @staticmethod
    def assert_is_selected(element: WebElement, is_selected: bool = True):
        assert element.is_selected() == is_selected, Asserter._err_message(is_selected, element.is_selected())

    @staticmethod
    def _err_message(expected, actual):
        return f'Expected {expected}, got {actual} instead'
