import random
from word_list import word_list
# import word_list --- usages word_list.word_list

chosen_word = random.choice(word_list)
chosen_word_place_holder = ""
display = ""
game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a char: ").lower()
    print(display)

    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(guess)
        elif char in correct_letters:
            print(f"you got this before, {char}")
            display += char
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"live loss, You have {lives}")
        if lives == 0:
            print("Game Lost")
            game_over = True

    if ("_") not in display:
        game_over = True
        print("Win")
