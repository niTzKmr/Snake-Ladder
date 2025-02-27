import tkinter as tk
from tkinter import messagebox
import random


snakes = {
    17: 7,  
    54: 34  
}

ladders = {
    4: 14,  
    9: 31   
}


BG_COLOR = "#F0F0F0"  
BUTTON_COLOR = "#4CAF50"  
TEXT_COLOR = "#333333"  
PLAYER1_COLOR = "#FF5733"  
PLAYER2_COLOR = "#33A2FF"  


def roll_dice():
    return random.randint(1, 6)


def check_snake_or_ladder(position):
    if position in snakes:
        messagebox.showinfo("Snake Bite!", f"Oops! Snake bite. You go down from {position} to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        messagebox.showinfo("Ladder Climb!", f"Yay! Ladder climb. You go up from {position} to {ladders[position]}")
        position = ladders[position]
    return position

def update_position(player):
    dice_value = roll_dice()
    dice_label.config(text=f"🎲 Player {player} rolled a {dice_value}")

    if player == 1:
        player1_position.set(player1_position.get() + dice_value)
        player1_position.set(check_snake_or_ladder(player1_position.get()))
        player1_label.config(text=f"Player 1: {player1_position.get()}", fg=PLAYER1_COLOR)
        if player1_position.get() >= 100:
            messagebox.showinfo("Game Over!", "🎉 Player 1 wins!")
            reset_game()
        else:
            current_player.set(2)
    else:
        player2_position.set(player2_position.get() + dice_value)
        player2_position.set(check_snake_or_ladder(player2_position.get()))
        player2_label.config(text=f"Player 2: {player2_position.get()}", fg=PLAYER2_COLOR)
        if player2_position.get() >= 100:
            messagebox.showinfo("Game Over!", "🎉 Player 2 wins!")
            reset_game()
        else:
            current_player.set(1)

    current_player_label.config(text=f"Current Player: {current_player.get()}", fg=PLAYER1_COLOR if current_player.get() == 1 else PLAYER2_COLOR)


def reset_game():
    player1_position.set(0)
    player2_position.set(0)
    current_player.set(1)
    player1_label.config(text="Player 1: 0", fg=PLAYER1_COLOR)
    player2_label.config(text="Player 2: 0", fg=PLAYER2_COLOR)
    current_player_label.config(text="Current Player: 1", fg=PLAYER1_COLOR)
    dice_label.config(text="🎲 Roll the dice!")


root = tk.Tk()
root.title("Snake and Ladder Game")
root.geometry("400x300") 
root.configure(bg=BG_COLOR)


player1_position = tk.IntVar(value=0)
player2_position = tk.IntVar(value=0)
current_player = tk.IntVar(value=1)


player1_label = tk.Label(root, text="Player 1: 0", font=("Arial", 16, "bold"), bg=BG_COLOR, fg=PLAYER1_COLOR)
player1_label.pack(pady=10)

player2_label = tk.Label(root, text="Player 2: 0", font=("Arial", 16, "bold"), bg=BG_COLOR, fg=PLAYER2_COLOR)
player2_label.pack(pady=10)


current_player_label = tk.Label(root, text="Current Player: 1", font=("Arial", 14), bg=BG_COLOR, fg=TEXT_COLOR)
current_player_label.pack(pady=10)


dice_label = tk.Label(root, text="🎲 Roll the dice!", font=("Arial", 14), bg=BG_COLOR, fg=TEXT_COLOR)
dice_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14, "bold"), bg=BUTTON_COLOR, fg="white", command=lambda: update_position(current_player.get()))
roll_button.pack(pady=20)


reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), bg=BUTTON_COLOR, fg="white", command=reset_game)
reset_button.pack(pady=10)


root.mainloop()