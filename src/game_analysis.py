def check_for_win():
    check_for_horizontal_win()
    check_for_vertical_win()
    check_for_diagonal_win()

def check_for_horizontal_win():
    for row in board:
        if all(row):
            print(f"The winner is {row[0]}")
            exit()

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