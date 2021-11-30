from time import sleep


def test_board_game_order(home_page, board_games_page, cart_popup, cart_page):
    home_page.validate_language()
    home_page.click_board_games_tab()

    board_games_page.validate_language()
    board_games_page.move_price_filter(50)
    board_games_page.move_players_number_filter(-100)
    board_games_page.choose_ua_games()
    board_games_page.accept_filter()

    for button in board_games_page.buy_buttons():
        button.click()
        cart_popup.click_continue_button()

    board_games_page.click_cart_button()
    cart_popup.click_order_button()

    cart_page.validate_language()
    cart_page.open_paper_chooser()

    sleep(3)
