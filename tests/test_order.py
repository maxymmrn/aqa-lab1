import allure


def test_board_game_order(home_page, board_games_page, cart_popup, cart_page, paper_chooser_popup):
    go_to_board_games(home_page)
    filter_games(board_games_page)
    select_games(board_games_page, cart_popup)
    choose_paper(cart_page, paper_chooser_popup)
    enter_payment_data(cart_page)


@allure.step
def go_to_board_games(home_page):
    home_page.validate_language()
    home_page.click_board_games_tab()


@allure.step
def filter_games(board_games_page):
    board_games_page.validate_language()
    board_games_page.move_price_filter(50)
    board_games_page.move_players_number_filter(-100)
    board_games_page.choose_ua_games()
    board_games_page.accept_filter()


@allure.step
def select_games(board_games_page, cart_popup):
    for button in board_games_page.buy_buttons():
        button.click()
        cart_popup.click_continue_button()

    board_games_page.click_cart_button()
    cart_popup.click_order_button()


@allure.step
def choose_paper(cart_page, paper_chooser_popup):
    cart_page.open_paper_chooser()
    paper_chooser_popup.choose_paper(2)
    paper_chooser_popup.choose_paper(5)
    paper_chooser_popup.confirm()
    cart_page.validate_paper_choice()


@allure.step
def enter_payment_data(cart_page):
    cart_page.validate_language()
    cart_page.enter_name('Максим')
    cart_page.enter_surname('Маріна')
    cart_page.enter_phone_number('+380939333401')
    cart_page.enter_email('maxymmrn@gmail.com')
    cart_page.choose_delivery_type()
    cart_page.choose_payment_type()