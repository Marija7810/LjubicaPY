def create_board():
    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']
    return board


def prepare_board_for_display(board):
    display_board_string = 'Koordinate su \n 1|2|3 \n 4|5|6 \n 7|8|9\n' + "--------------\n" +\
                            board[0] + '|' + board[1] + '|' + board[2] + "\n" + \
                            board[3] + '|' + board[4] + '|' + board[5] + "\n" +\
                            board[6] + '|' + board[7] + '|' + board[8] + "\n"
    return display_board_string


def read_position(board):
    valid = False
    position = '0'
    while not valid:
        position = input("Odabrati poziciju od 1 do 9:")
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Odabrati poziciju od 1 do 9:")
        position = int(position) - 1
        if board[position] == '-':
            valid = True
    return position


def play_turn(player, board, position):
    board[position] = player
    return board


def switch_player(player):
    if player == 'x':
        player = 'o'
    elif player == 'o':
        player = 'x'
    return player


def winner_by_rows(board):
    winner = None
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1:
        winner = board[0]
    if row_2:
        winner = board[3]
    if row_3:
        winner = board[6]
    return winner


def winner_by_columns(board):
    winner = None
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    if column_1:
        winner = board[0]
    if column_2:
        winner = board[1]
    if column_3:
        winner = board[2]
    return winner


def winner_by_diagonals(board):
    winner = None
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'
    if diagonal_1:
        winner = board[0]
    if diagonal_2:
        winner = board[2]
    return winner


def get_winner(board):
    winner = None
    if winner_by_rows(board) is not None:
        winner = winner_by_rows(board)
    elif winner_by_columns(board) is not None:
        winner = winner_by_columns(board)
    elif winner_by_diagonals(board) is not None:
        winner = winner_by_diagonals(board)
    return winner


def has_winner(board):
    if get_winner(board) is not None:
        return True
    return False


def is_a_tie(board):
    if '-' not in board:
        return True
    return False


def is_game_on(board):
    if has_winner(board):
        return False
    if is_a_tie(board):
        return False
    return True


def main():
    while True:
        player = 'x'
        board = create_board()
        print(prepare_board_for_display(board))
        while is_game_on(board):
            print("Na redu je: " + player)
            position = read_position(board)
            board = play_turn(player, board, position)
            print(prepare_board_for_display(board))
            if has_winner(board):
                print("Pobedio je: " + player)
            if is_a_tie(board):
                print("Nereseno je.\n")
            player = switch_player(player)
        continue_game = input('Da li zelite da nastavite igru(Y,N):')
        while continue_game not in ['Y', 'y', 'n', 'N']:
            continue_game = input('Pogresan unos! Da li zelite da nastavite igru(Y,N):')
        if continue_game == 'N' or continue_game == 'n':
            break
