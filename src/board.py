from players import Players

class Board:

    global board 
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def create_board(self):
        return board 

    def display_board(self):
        print("\n")
        print(Players(board[0][0]).name + "|" + Players(board[0][1]).name + "|" + Players(board[0][2]).name)
        print(Players(board[1][0]).name + "|" + Players(board[1][1]).name + "|" + Players(board[1][2]).name)
        print(Players(board[2][0]).name + "|" + Players(board[2][1]).name + "|" + Players(board[2][2]).name)