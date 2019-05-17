from players import Players
from board import Board

global active_player
active_player = Players.X
global board

def play_game():
    start_game()
    while True:
        play_round()

def start_game():
    create_board()
    display_board()

def create_board():
    global board
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def play_round():
    place_piece()
    display_board()
    check_for_win()

def display_board():
    print("\n")
    print(Players(board[0][0]).name + "|" + Players(board[0][1]).name + "|" + Players(board[0][2]).name)
    print(Players(board[1][0]).name + "|" + Players(board[1][1]).name + "|" + Players(board[1][2]).name)
    print(Players(board[2][0]).name + "|" + Players(board[2][1]).name + "|" + Players(board[2][2]).name)

def place_piece():
    index = int(input("\nPlease enter a number 1-9: "))
    if index > 6:
        board[2][index - 7] = active_player
    elif index > 3:
        board[1][index - 4] = active_player
    else:
        board[0][index - 1] = active_player
        
    switch_active_player()

def switch_active_player():
    global active_player
    active_player = Players.O if active_player is Players.X else Players.X

def check_for_win():
    check_for_horizontal_win()
    check_for_vertical_win()
    check_for_diagonal_win()

def check_for_horizontal_win():
    for row in board:
        if row_is_matching(row) and row[0] is not 0:
            print(f"The winner is {row[0]}")
            exit()

def row_is_matching(row):
    row_iterator = iter(row)
    try:
        first = next(row_iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in row_iterator)

def check_for_vertical_win():
    itr = 0
    
    for square in board[0]:
        if column_is_matching(itr, square):
            print(f"The winner is {square}")
            exit()

def column_is_matching(itr, square):
    if square is board[1][itr] and square is board[2][itr] and square is not 0:
        itr = itr + 1
        return True
    else:
        itr = itr + 1
        return False

def check_for_diagonal_win():
    check_top_left_diagonal()
    check_top_right_diagonal()

def check_top_left_diagonal():
    if board[0][0] is board[1][1] and board[0][0] is board[2][2] and board[0][0] is not 0:
        print(f"The winner is {board[0][0]}")
        exit()

def check_top_right_diagonal():
    if board[0][2] is board[1][1] and board[0][2] is board[2][0] and board[0][2] is not 0:
        print(f"The winner is {board[0][2]}")
        exit()


play_game()