from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    print(computer_choice)

    if player_choice == computer_choice:
        print ('Draw!')
    elif player_choice == 'rock' or computer_choice == 'scissors':
        win()
    elif  player_choice== 'paper' or computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' or computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' or computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' or computer_choice == 'rock':
        win()
    elif player_choice == 'rock' or computer_choice == 'paper':
        lose()
    aGain = input('Do you want to play again? (y or n)').strip()
    if aGain == 'n':
        break 

# import random

# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     possible_actions = ["rock", "paper", "scissors"]
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         break
