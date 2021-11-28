from time import sleep


def test_board_game_order(home_page, board_games_page):
    home_page.validate_language()
    home_page.validate_board_games_tab()
    home_page.click_board_games_tab()

    board_games_page.validate_language()
    board_games_page.move_price_filter(50)
    board_games_page.move_players_number_filter(-100)
    board_games_page.choose_ua_games()
    board_games_page.accept_filter()
    sleep(10)

