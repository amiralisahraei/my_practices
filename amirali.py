import random
from config import GAME_CHOICES, RULES, scoreboard


def get_user_choice():
    user_input = input("Enter your choice (r, s, p) : ")
    if user_input  not in GAME_CHOICES:
        print("OOps ..!")
        return get_user_choice()
    return user_input


def get_system_choice():
    return random.choice(GAME_CHOICES)

def find_winner(user, system):
    match = {user, system}

    if len(match) == 1:
        return None
    return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
        msg = "You win"
    else:
        scoreboard['system'] += 1
        msg = "You lose"

    print('#'*20)
    print("##", f"user: {scoreboard['user']}".ljust(14), "##")
    print("##", f"system: {scoreboard['system']}".ljust(14), "##")
    print("##", f"last game: {msg}".ljust(14), "##")
    print('#'*20)


def play():

    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_input = get_user_choice()
        system_input = get_system_choice()
        winner = find_winner(user_input, system_input)

        if winner == user_input:
            msg = "You win"
            result['user'] += 1
        elif winner == system_input:
            msg = "You lose"
            result['system'] += 1
        else:
            msg = "Draw"

        print(f"user: {user_input} \t system: {system_input} \t result: {msg}")
        print(result)
    
    update_scoreboard(result)
    play_again = input("Would you like play again ?? (y/n)")
    if play_again == 'y':
        play()

if __name__ == "__main__":
    play()