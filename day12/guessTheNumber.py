import random
number_to_guess = random.randint(0, 100)

print("============================================\nWelcome to Number Guessing Game\n============================================\nI am thinking of a number between 1 - 100 \nCan you guess it?")


def start_game():
    ready = input("\nReady to start? (yes/no): ").lower()
    if ready == "yes" or ready == "y":
        return True
        print("Let\'s Start!")
    elif ready == "no" or ready == "n":
        print("See You Later!")
        return False
    else:
        print("Wrong Command! Try again ...")
        return start_game()

ready = start_game()

def play_game():
    level = input("Chose your difficulty level (easy/medium/hard): ").lower()
    attempts = [10,7,5]
    game_over = False
    attempts_left = 0

    def find_user_level():
        if level == "h" or level == "hard":
            print(f"All right, Hard difficulty it is!!\nYou will get {attempts[2]} attempts to guess")
            return 2 #hard
        if level == "m" or level == "medium":
            print(f"All right, Medium difficulty it is!!\nYou will get {attempts[1]} attempts to guess")
            return 1 #medium
        if level == "e" or level == "easy":
            print(f"All right, Easy difficulty it is!!\nYou will get {attempts[0]} attempts to guess")
            return 0 #easy
        else:
            print("Wrong Command! Try again ...")
            return -1

    user_level = find_user_level()

    if user_level == 2:
        attempts_left = attempts[user_level]
    elif user_level == 1:
        attempts_left = attempts[user_level]
    elif user_level == 0:
        attempts_left = attempts[user_level]
    else:
        find_user_level()

    def compare_number(user_number, number_to_guess):
        if user_number > number_to_guess:
            print("~ Computer: Your number is bigger then mine")
            return -1
        elif user_number < number_to_guess:
            print("~ Computer: Your number is smaller then mine")
            return -1
        elif user_number == number_to_guess:
            print("You Found The Number\nYou Are a winner\n=======================================\nCongratulations!\n=======================================")
            game_over = True
            return 0
        else:
            print("Not a number!")
            return -1

    while not game_over:
        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left")
            guessed_number = int(input("Write your guess: "))
            found_number = compare_number(guessed_number, number_to_guess)

            if found_number == -1:
                attempts_left -= 1
            else:
                game_over = True
        else:
            game_over = True
            print("You are out of attempts!\nYou Lose :(\nBetter luck next time.")


if ready:
    user_level = play_game()