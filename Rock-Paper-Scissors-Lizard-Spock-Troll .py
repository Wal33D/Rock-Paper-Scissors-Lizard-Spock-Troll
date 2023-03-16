# Rock-Paper-Scissors-Lizard-Spock-Troll Game
# Author: Waleed Judah
# Date: 3/8/2023
# This program implements a game that allows users to play Rock-Paper-Scissors-Lizard-Spock-Troll against a computer.
# The game uses several libraries such as `random`, `json`, `winsound`, and `termcolor` to enhance the user experience.
# The program also keeps track of scores and allows the user to view scores and players, as well as add new players.

import random
import json
import winsound
from termcolor import colored

# Define the game name and options
GAME_NAME = "Rock-Paper-Scissors-Lizard-Spock-Troll"
OPTIONS = ["rock", "paper", "scissors", "lizard", "spock"]
WINNING_CHOICES = {
    '\033[31mrock\033[0m': ['\033[32mpaper\033[0m', '\033[36mspock\033[0m', 'paper', 'spock'],
    '\033[32mpaper\033[0m': ['\033[34mscissors\033[0m', '\033[35mlizard\033[0m', 'scissors', 'lizard'],
    '\033[34mscissors\033[0m': ['\033[31mrock\033[0m', '\033[36mspock\033[0m', 'rock', 'spock'],
    '\033[35mlizard\033[0m': ['\033[31mrock\033[0m', '\033[34mscissors\033[0m', 'rock', 'scissors'],
    '\033[36mspock\033[0m': ['\033[32mpaper\033[0m', '\033[35mlizard\033[0m', 'paper', 'lizard']
}

PHRASES = ["I'm sorry, I didn't understand that. Please try again!", "That wasn't a valid input. Please try again!", "I'm not sure what you meant. Please try again!"]
SCORES_FILE = "scores.json"

def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file)

def load_data(file_name, default):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        if not data:
            data = default
        return data
    except FileNotFoundError:
        return default

# Load scores from file or create an empty dict if file not found
SCORES = load_data(SCORES_FILE, {})


def display_menu():
    print(colored(" _______________________________________________ ", "yellow"))
    print(colored("|                                               |", "yellow"))
    print(colored("| ▲  Rock-Paper-Scissors-Lizard-Spock-Troll ▲   |", "magenta"))
    print(colored("|                                               |", "yellow"))
    print(colored("|                 MAIN MENU                     |", "cyan"))
    print(colored("|                                               |", "yellow"))
    print(colored("|", "yellow"), colored(" [1] ", "red"), colored("        Play                            |", "yellow"))
    print(colored("|", "yellow"), colored(" [2] ", "red"), colored("        View Scores                     |", "yellow"))
    print(colored("|", "yellow"), colored(" [3] ", "red"), colored("        Players                         |", "yellow"))
    print(colored("|", "yellow"), colored(" [4] ", "red"), colored("        End Game                        |", "yellow"))
    print(colored("|                                               |", "yellow"))
    print(colored("|_______________________________________________|", "yellow"))
    return input(colored("Enter your choice (1-4): ", "green"))

def add_user():
    global SCORES
    print(colored("  _______________________________________________ ", "yellow"))
    print(colored(" /                                               \\", "yellow"))
    print(colored("|              ADD USER                           |", "magenta"))
    print(colored(" \\_______________________________________________/", "yellow"))
    name = input(colored("\nEnter the name of the new user:\n", "green"))
    if name in SCORES:
        print(colored("User already exists.", "red"))
    else:
        SCORES[name] = {'player': 0, 'computer': 0}
        save_data(SCORES_FILE, SCORES)

def display_scores():
    global SCORES
    print(colored("  _______________________________________________ ", "yellow"))
    print(colored(" /                                               \\", "yellow"))
    print(colored("|             SCORES                              |", "magenta"))
    print(colored("|                                                 |", "yellow"))
    for user, score in SCORES.items():
        print(colored(f"          {user}: {score}{' '*(28-len(user)-len(str(score)))}", "cyan"))
    print(colored("|                                                 |", "yellow"))
    print(colored("|_________________________________________________|", "yellow"))
    print()


def display_players_menu():
    print(colored(" _______________________________________________ ", "yellow"))
    print(colored("|                                               |", "yellow"))
    print(colored("| ▼  Rock-Paper-Scissors-Lizard-Spock-Troll  ▼  |", "magenta"))
    print(colored("|                                               |", "yellow"))
    print(colored("|             PLAYERS                           |", "cyan"))
    print(colored("|                                               |", "yellow"))
    print(colored("|              [1] View All Players             |", "red"))
    print(colored("|              [2] Add New Player               |", "red"))
    print(colored("|              [3] Back to Main Menu            |", "red"))
    print(colored("|                                               |", "yellow"))
    print(colored("|_______________________________________________|", "yellow"))
    return input(colored("Enter your choice (1-3): ", "green"))

def display_users():
    global USERS
    print(colored("  _______________________________________________ ", "yellow"))
    print(colored(" /                                               \\", "yellow"))
    print(colored("|              USERS                              |", "magenta"))
    print(colored("|                                                 |", "yellow"))
    for user in SCORES.keys():
        print(colored(f"                {user}{' '*(44-len(user))}", "cyan"))
    print(colored("|                                                 |", "yellow"))
    print(colored("|_________________________________________________|", "yellow"))
    print()

def play_game(user):
    global SCORES
    if user not in SCORES:
        SCORES[user] = {'player': 0, 'computer': 0}
    while True:
        computer_choice = OPTIONS[random.randint(0, 4)]
        user_choice = input(colored(f"{user}, enter your choice (", "yellow") + 
                           colored("rock", "red") + colored(", ", "yellow") + 
                           colored("paper", "green") + colored(", ", "yellow") + 
                           colored("scissors", "blue") + colored(", ", "yellow") + 
                           colored("lizard", "magenta") + colored(", ", "yellow") + 
                           colored("spock", "cyan") + colored("), or type 'quit' to end the game: ", "yellow"))
        if user_choice.lower() == 'quit':
            print(f'Final score: {user}: {SCORES[user]["player"]} - Computer: {SCORES[user]["computer"]}\n')
            break
        elif user_choice.lower() not in [option.lower() for option in OPTIONS]:
            print(random.choice(PHRASES))
            continue
        user_choice = user_choice.lower()
        if computer_choice == "rock":
            computer_choice = colored(computer_choice, 'red')
        elif computer_choice == "paper":
            computer_choice = colored(computer_choice, 'green')
        elif computer_choice == "scissors":
            computer_choice = colored(computer_choice, 'blue')
        elif computer_choice == "lizard":
            computer_choice = colored(computer_choice, 'magenta')
        else:
            computer_choice = colored(computer_choice, 'cyan')
        print(f"The computer chose: {computer_choice}")
        if user_choice == computer_choice.lower().strip():
            print("It's a tie!")
        elif user_choice in [choice.lower().strip() for choice in WINNING_CHOICES[computer_choice.lower().strip()]] or \
   user_choice in WINNING_CHOICES[computer_choice.lower().strip()]:
            print(colored(f"{user} wins!", "red") + colored("!", "green") + colored("!", "yellow") + colored("!", "blue"))
            winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
            SCORES[user]['player'] += 1
        else:
            print("The computer wins.")
            SCORES[user]['computer'] += 1
        print(f"{user}: {SCORES[user]['player']} - Computer: {SCORES[user]['computer']}\n")
        with open(SCORES_FILE, "w") as file:
            json.dump(SCORES, file)

while True:
    choice = display_menu()
    winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
    if choice == '1':
        user = input("Enter your name:\n▶️  ")
        if user not in SCORES:
            SCORES[user] = {'player': 0, 'computer': 0}
            save_data(SCORES_FILE, SCORES)
        winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
        play_game(user)  # pass the user name as an argument
    elif choice == '2':
        winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
        display_scores()
    elif choice == '3':
        while True:
            players_choice = display_players_menu()
            if players_choice == '1':
                winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
                display_users()
            elif players_choice == '2':
                winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
                add_user()
            elif players_choice == '3':
                winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
                break
            else:
                print("Invalid input. Please enter a number from 1 to 3.\n")
    elif choice == '4':
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print(f"Thanks for playing {GAME_NAME}!")
        break
    else:
        print("Invalid input. Please enter a number from 1 to 4.\n")
        winsound.PlaySound(winsound.MB_ICONERROR, winsound.SND_ASYNC)