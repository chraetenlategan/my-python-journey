
def DisplayBoard(board):
    for r in range(8):
        board_order = ""
        for c in range(8):
            board_order += board[r][c]
        print(board_order)


def check_turns(number_of_moves):
    if number_of_moves%2 == 0:
        return("white_turn")
    else:
        return("black_turn")

def check_available_moves(board):
    pass
    

