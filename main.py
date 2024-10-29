import tkinter as tk
from tkinter import messagebox
import random

#initialize the game window
root = tk.Tk()
root.title('Tic Tac Toe')


#veriable to track the game
current_player = "X"
board = [' ' for _ in range(9)]

win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals

def on_click(idx):
    global current_player
    if board[idx] == ' ':
        board[idx] = current_player
        buttons[idx].config(text=current_player)
        result = check_game_status()
        if result:
            show_result(result)
        else:
            toggle_player()

# Function to toggle between players
def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    if current_player == "O":  # Bot's turn
        user_bot()

# Function to check game status (win, tie, or ongoing)
def check_game_status():
    winner = check_winner()
    if winner:
        return f"Player {winner} wins!"
    elif tie_check():
        return "It's a tie!"
    return None  # Game is still ongoing

# Function to check for a winner
def check_winner():
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return board[condition[0]]  # Return 'X' or 'O' as the winner
    return None


#create bot function to play automatic
def user_bot():
    global current_player
    # Ensure it's the bot's turn
    if current_player == "O" and ' ' in board:
        x_block_position = track_winning("X")
        o_winning_position = track_winning("O")
        if o_winning_position is not None:
            board[o_winning_position] = current_player
            buttons[o_winning_position].config(text=current_player)
        elif x_block_position is not None:
            board[x_block_position] = current_player
            buttons[x_block_position].config(text=current_player)
        else:
            blank_index = [index for index, value in enumerate(board) if value == ' ']
            pick_position = random.choice(blank_index)
            board[pick_position] = current_player
            buttons[pick_position].config(text=current_player)


        # Check the game status after the bot's move
        result = check_game_status()
        if result:
            show_result(result)
        else:
            toggle_player()  # Switch back to the user


#track user winning movement
def track_winning(player):
    for condition in win_conditions:
        values = [board[i] for i in condition]
        if values.count(player) == 2 and values.count(' ') == 1:
            return condition[values.index(' ')]

    return None


# Function to check if it's a tie
def tie_check():
    return ' ' not in board

# Function to show the result
def show_result(message):
    messagebox.showinfo("Tic Tac Toe", message)
    reset_game()


#function for create reset the game
def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text='')


#create the Tic tac Toe game using button

button_frame = tk.Frame()
button_frame.grid(row=1, column=0, padx=10, pady=20)
buttons = []
for i in range(9):
    button = tk.Button(root, text='', font=('Arial', 20), width=5, height=2,
                       command=lambda idx=i: on_click(idx))
    button.grid(row=(i//3), column=i % 3)
    buttons.append(button)

root.mainloop()
