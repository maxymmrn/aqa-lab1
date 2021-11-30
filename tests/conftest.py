from pytest import fixture

from framework.driver.connection import Connection
from framework.driver.driver_factory import Browser
from framework.pages.board_games_page import BoardGamesPage
from framework.pages.cart_page import CartPage
from framework.pages.cart_popup import CartPopup
from framework.pages.home_page import HomePage


@fixture
def _connection():
    connection = Connection(browser=Browser.CHROME)
    yield connection
    connection.kill_session()


@fixture
def home_page(_connection) -> HomePage:
    return HomePage(_connection)


@fixture
def board_games_page(_connection):
    return BoardGamesPage(_connection)


@fixture
def cart_popup(_connection):
    return CartPopup(_connection)


@fixture
def cart_page(_connection):
    return CartPage(_connection)
