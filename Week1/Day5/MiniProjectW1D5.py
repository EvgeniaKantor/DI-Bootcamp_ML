# The game is played on a grid that’s 3 squares by 3 squares.
print('Welcome to TIC TAC TOE!\n')

# Function to display the game board
def display_board(board):
    print('TIC  TAC  TOE')
    print('*************')
    print('*', board[0][0], '|', board[0][1], '|', board[0][2], '*')
    print('*---|---|---*')
    print('*', board[1][0], '|', board[1][1], '|', board[1][2], '*')
    print('*---|---|---*')
    print('*', board[2][0], '|', board[2][1], '|', board[2][2], '*')
    print('*************')


# Take player input
def player_input(player, board):
    while True:
        try:
            row = int(input(f"Player {player}, enter the number of the row (1-3): "))
            column = int(input(f"Player {player}, enter the number of the column (1-3): "))
            if row < 1 or row > 3 or column < 1 or column > 3:
                print("Invalid input, please pick numbers between 1 and 3.")
                continue
            if board[row - 1][column - 1] != " ":
                print("This cell is already occupied! Choose another.")
                continue
            return (row - 1, column - 1)
        except ValueError:
            print("Invalid input! Please enter integers.")
            continue

# Function to check for a winner
def check_win(board, marker):
    for row in range(3):
        if all([board[row][col] == marker for col in range(3)]):
            return True
    for col in range(3):
        if all([board[row][col] == marker for row in range(3)]):
            return True
    if board[0][0] == marker and board[1][1] == marker and board[2][2] == marker:
        return True
    if board[0][2] == marker and board[1][1] == marker and board[2][0] == marker:
        return True
    return False
           
# Main function to run the game
def play():
    board = [[" ", " ", " "], 
             [" ", " ", " "], 
             [" ", " ", " "]]

    display_board(board)
    currentPlayer = "X"
    
    for turn in range(9):
        print(f"Player {currentPlayer}'s turn")
        row, col = player_input(currentPlayer, board)
        board[row][col] = currentPlayer
        display_board(board)

        if check_win(board, currentPlayer):
            print(f"Player {currentPlayer} wins!")
            break

        # Change player for next turn
        currentPlayer = "O" if currentPlayer == "X" else "X"
    else:
        print("It's a tie!")

# Start the game
play()
