import data
import random
game_over = True

print("===============================================")
print("Welcome to higher lower game!")
print("===============================================")
print("\n\n")
show_instruction = input("Do you like to view rules how to play this game? (yes/no): ").lower()

if show_instruction == "yes" or show_instruction == "y":
    print("In this game you have to guess between two celebrities who has more follower. You have to choose your option using A/B. If you choose correctly you will continue game otherwise game over! Hope you get the rules!")
elif show_instruction == "no" or show_instruction == "n":
    print("All right hope you know the rules")
else:
    print("Wrong Command, Skipping")

start_play = input("\nReady To Start? (yes/no): ").lower()

if start_play == "yes" or start_play == "y":
    print("Let's Start")
    game_over = False
elif start_play == "no" or start_play == "n":
    print("Ok! Play when you get time")
else:
    print("Wrong Command, Skipping")

def getChoice(previous_choice = None):
    choices = []
    first_choice = {}
    second_choice = {}
    if previous_choice == None:
        first_choice = random.choice(data.celebrities)
        choices.append(first_choice)
    else:
        first_choice = previous_choice
        choices.append(previous_choice)

    second_choice = random.choice(data.celebrities)

    if data.celebrities.index(first_choice) != data.celebrities.index(second_choice):
        choices.append(second_choice)
    else:
        return getChoice(first_choice)

    return choices

user_options = getChoice()
user_score = 0
user_attempt = 0

while not game_over:
    print(f"Your current score is {user_score}")
    user_attempt += 1
    if user_attempt > 0:
        user_options = getChoice(user_options[0])

    print(f"   A: {user_options[0]["name"]} is a {user_options[0]["profession"]} from {user_options[0]["country"]}")
    print(f"   B: {user_options[1]["name"]} is a {user_options[1]["profession"]} from {user_options[1]["country"]}")
    print(f"{user_options[0]["name"]} has {user_options[0]["followers"]} million followers. What do you think {user_options[1]["name"]} has higher or lower followers?")

    user_response = input("~ Write higher/lower: ").lower()

    if user_response == "higher" or user_response == "h":
        print("You said higher.")
        if user_options[1]["followers"] >= user_options[0]["followers"]:
            print("You are right")
            user_score += 1
        else:
            game_over = True
            print("You are Wrong!\nGame Over\nBetter Luck Next Time!")
            print(f"============== Your Final Score Was: {user_score} ===============")
    elif user_response == "lower" or user_response == "l":
        print("You said lower.")
        if user_options[1]["followers"] <= user_options[0]["followers"]:
            print("You are right")
            user_score += 1
        else:
            game_over = True
            print("You are Wrong!\nGame Over\nBetter Luck Next Time!")
            print(f"============== Your Final Score Was: {user_score} ===============")
    else:
        print("Wrong keyword! We are auto selecting lower")
        if user_options[1]["followers"] <= user_options[0]["followers"]:
            print("You are right")
            user_score += 1
        else:
            game_over = True
            print("You are Wrong!\nGame Over\nBetter Luck Next Time!")
            print(f"============== Your Final Score Was: {user_score} ===============")