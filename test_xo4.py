import xo4_fcn
import pytest


class TestXO(object):
    def test_create_board(self):
        assert xo4_fcn.create_board() == ['-', '-', '-',
                                          '-', '-', '-',
                                          '-', '-', '-']

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', '-', 'x', 'x', '-', '-', '-']),
                                 (['x', 'x', 'o', 'o', 'x', 'o', 'o', 'o', 'x'])
                             ])
    def test_prepare_board_for_display(self, par_board):
        assert xo4_fcn.prepare_board_for_display(par_board) == 'Koordinate su \n 1|2|3 \n 4|5|6 \n 7|8|9\n' + \
               "--------------\n" + \
               par_board[0] + '|' + par_board[1] + '|' + par_board[2] + \
               "\n" + \
               par_board[3] + '|' + par_board[4] + '|' + par_board[5] + \
               "\n" + \
               par_board[6] + '|' + par_board[7] + '|' + par_board[8] + \
               "\n"

    def test_play_turn(self):
        player = 'x'
        position = 3
        board = ['o', 'x', 'x', '-', '-', '-', '-', '-', '-']
        assert xo4_fcn.play_turn(player, board, position) == ['o', 'x', 'x', 'x', '-', '-', '-', '-', '-']

    def test_switch_player(self):
        assert xo4_fcn.switch_player('x') == 'o'
        assert xo4_fcn.switch_player('o') == 'x'

    @pytest.mark.parametrize('par_board',
                             [
                                 (['x', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', 'x', 'x', 'x', '-', '-', '-']),
                                 (['-', '-', '-', '-', '-', '-', 'x', 'x', 'x'])

                             ])
    def test_winner_by_rows(self, par_board):
        winner = xo4_fcn.winner_by_rows(par_board)
        assert winner == 'x'

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', '-', 'x', 'x', '-', '-', '-']),
                                 (['x', 'x', 'o', 'o', 'x', 'o', 'o', 'x', 'x'])

                             ])
    def test_no_winner_by_rows(self, par_board):
        winner = xo4_fcn.winner_by_rows(par_board)
        assert winner is None

    @pytest.mark.parametrize('par_board',
                             [
                                 (['x', '-', '-', 'x', '-', '-', 'x', '-', '-']),
                                 (['o', 'x', '-', 'o', 'x', '-', '-', 'x', '-']),
                                 (['o', 'x', 'x', 'x', 'o', 'x', 'x', 'o', 'x'])

                             ])
    def test_winner_by_columns(self, par_board):
        winner = xo4_fcn.winner_by_columns(par_board)
        assert winner == 'x'

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', '-', 'x', 'x', '-', '-', '-']),
                                 (['x', 'x', 'o', 'o', 'x', 'o', 'o', 'o', 'x'])

                             ])
    def test_no_winner_by_columns(self, par_board):
        winner = xo4_fcn.winner_by_columns(par_board)
        assert winner is None

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', '-', '-', '-', 'o', '-', '-', '-', 'o']),
                                 (['x', 'o', 'o', 'o', 'o', 'x', 'o', 'x', 'x'])
                             ])
    def test_winner_by_diagonals(self, par_board):
        winner = xo4_fcn.winner_by_diagonals(par_board)
        assert winner == 'o'

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', '-', 'x', 'x', '-', '-', '-']),
                                 (['o', 'x', 'o', 'o', 'x', 'o', 'o', 'o', 'x'])

                             ])
    def test_no_winner_by_diagonals(self, par_board):
        winner = xo4_fcn.winner_by_diagonals(par_board)
        assert winner is None

    @pytest.mark.parametrize('par_board',
                             [
                                 (['x', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', 'x', 'x', 'x', '-', '-', '-']),
                                 (['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x'])

                             ])
    def test_get_winner_rows(self, par_board):
        winner = xo4_fcn.get_winner(par_board)
        assert winner == 'x'

    @pytest.mark.parametrize('par_board',
                             [
                                 (['x', '-', '-', 'x', '-', '-', 'x', '-', '-']),
                                 (['o', 'x', '-', 'o', 'x', '-', '-', 'x', '-']),
                                 (['o', 'x', 'x', 'x', 'o', 'x', 'x', 'o', 'x'])

                             ])
    def test_get_winner_columns(self, par_board):
        winner = xo4_fcn.get_winner(par_board)
        assert winner == 'x'

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', '-', '-', '-', 'o', '-', '-', '-', 'o']),
                                 (['x', 'o', 'o', 'o', 'o', 'x', 'o', 'x', 'x'])
                             ])
    def test_get_winner_diagonals(self, par_board):
        winner = xo4_fcn.get_winner(par_board)
        assert winner == 'o'

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', '-', 'x', 'x', '-', '-', '-']),
                                 (['o', 'x', 'o', 'o', 'x', 'o', 'x', 'o', 'x'])

                             ])
    def test_get_winner_none(self, par_board):
        winner = xo4_fcn.get_winner(par_board)
        assert winner is None

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', '-', '-', '-', 'o', '-', '-', '-', 'o']),
                                 (['x', 'o', 'o', 'o', 'o', 'x', 'o', 'x', 'x'])
                             ])
    def test_has_winner(self, par_board):
        assert xo4_fcn.has_winner(par_board) is True

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', '-', 'x', 'x', '-', '-', '-']),
                                 (['o', 'x', 'o', 'o', 'x', 'o', 'x', 'o', 'x'])

                             ])
    def test_has_no_winner(self, par_board):
        assert xo4_fcn.has_winner(par_board) is False

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', 'x', 'x', 'x', 'o', 'x', 'o', 'o', 'x']),
                                 (['o', 'x', 'o', 'o', 'x', 'o', 'x', 'o', 'x'])

                             ])
    def test_is_a_tie(self, par_board):
        assert xo4_fcn.is_a_tie(par_board) is True

    @pytest.mark.parametrize('par_board',
                             [
                                 (['-', 'x', 'x', 'x', 'o', 'x', 'o', 'o', 'x']),
                                 (['o', 'x', '-', 'x', '-', '-', 'x', 'x', 'x'])

                             ])
    def test_is_not_a_tie(self, par_board):
        assert xo4_fcn.is_a_tie(par_board) is False

    @pytest.mark.parametrize('par_board',
                             [
                                 (['o', 'x', 'x', 'x', 'o', 'x', 'o', 'o', 'x']),
                                 (['x', 'x', 'x', '-', '-', '-', '-', '-', '-']),
                                 (['o', 'x', 'x', 'x', 'o', 'x', 'x', 'o', 'x']),
                                 (['x', 'o', 'o', 'o', 'o', 'x', 'o', 'x', 'x'])

                             ])
    def test_game_not_on(self, par_board):
        assert xo4_fcn.is_game_on(par_board) is False

    @pytest.mark.parametrize('par_board',
                             [
                                 (['x', 'x', 'o', '-', '-', '-', '-', '-', '-']),
                                 (['-', '-', '-', '-', 'x', 'x', '-', '-', '-']),
                                 (['o', 'x', 'o', 'o', '-', 'o', 'x', 'o', 'x'])

                             ])
    def test_game_on(self, par_board):
        assert xo4_fcn.is_game_on(par_board) is True
