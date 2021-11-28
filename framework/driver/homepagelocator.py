from enum import Enum


class Locator(str, Enum):
    BOARD_GAMES_TAB = '//*[@id="menu"]/div[2]/ul/li[1]/a'
    UA_LANGUAGE_BUTTON = '//*[@id="form-language"]/ul/li[1]/a'
    FILTER_SECTION = '//*[@id="rdrf36"]'
    MONEY_FILTER = '//*[@id="rdrf36-price-group"]/div/span/span[6]'
    PLAYERS_NUMBER_FILTER = '//*[@id="rdrf36-attr15-group"]/div/span/span[7]'
    UA_LANGUAGE_FILTER = '//*[@id="rdrf36-attr16-5269f4d75f5bc75f0f94bab2100a5531"]/label'
    ACCEPT_FILTER_BUTTON = '//*[@id="rdrf-form36"]/div[2]/button[2]'
