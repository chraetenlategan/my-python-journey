from chess_function import DisplayBoard,check_available_moves,check_turns

# The chess board is added into a 2D list
board = [
    ["r","n","b","q","k","b","n","r"], 
    ["p","p","p","p","p","p","p","p"], 
    [".",".",".",".",".",".",".","."], 
    [".",".",".",".",".",".",".","."], 
    [".",".",".",".",".",".",".","."], 
    [".",".",".",".",".",".",".","."], 
    ["P","P","P","P","P","P","P","P"], 
    ["R","N","B","Q","K","B","N","R"], 
]
#Displays what colour turn
count_moves = 0
print(check_turns(count_moves))

# Display the initial board state
DisplayBoard(board)

# Check for the availible moves

