import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def button_click(row, col):
    global currentPlayer, winner_found  # Declare both as global variables
    if board[row][col] == " " and not winner_found:
        board[row][col] = currentPlayer
        buttons[row][col].config(text=currentPlayer, state="disabled")
        if check_win():
            messagebox.showinfo("Game Over", f"Player {currentPlayer} wins!")
            winner_found = True
        elif all(board[r][c] != " " for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            winner_found = True
        else:
            currentPlayer = "O" if currentPlayer == "X" else "X"

# Function to check if the current player wins
def check_win():
    # Check rows, columns, and diagonals
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != " ":
            return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Reset the game
def reset_game():
    global currentPlayer, winner_found
    currentPlayer = "X"
    winner_found = False
    for r in range(3):
        for c in range(3):
            board[r][c] = " "
            buttons[r][c].config(text=" ", state="normal")

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize board and buttons
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
currentPlayer = "X"
winner_found = False

# Create the grid of buttons
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text=" ", width=10, height=3, font=('normal', 24), 
                                  command=lambda r=r, c=c: button_click(r, c))
        buttons[r][c].grid(row=r, column=c)

# Create the reset button
reset_button = tk.Button(root, text="Reset", width=10, height=2, font=('normal', 16), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Run the application
root.mainloop()
