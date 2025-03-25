# Ms. Liu
# 7th Grade Computer Science
# 3/20/2025
# Rock, Paper, Scissors Game
# This program lets the player compete against the computer in a simple game.
import random  # Import the random module

# Define possible choices
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")

# Get player choice
player_choice = input("Enter rock, paper, or scissors: ").lower()

if player_choice == "rock":
    pass  # This allows the program to continue
elif player_choice == "paper":
    pass  # This allows the program to continue
elif player_choice == "scissors":
    pass  # This allows the program to continue
else:
    print("Invalid choice! Please enter rock, paper, or scissors.")
    quit()

# Get computer choice using random index
computer_index = random.randint(0, 2)  
computer_choice = choices[computer_index]  # Access choice from list

# Display choices
print("You chose:", player_choice)
print("Computer chose:", computer_choice)

# Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
    (player_choice == "paper" and computer_choice == "rock") or \
    (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")
    