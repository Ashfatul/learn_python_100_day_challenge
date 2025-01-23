import random

word_list = ["apple", "beach", "dream", "earth", "flame", "grape", "happy", "index", "jolly", "kites", "lemon", "mango", "notes", "ocean", "pearl", "quest", "roses", "stars", "tiger", "unity"]

your_word = random.choice(word_list)
lives = 5
word_placeholder = ""
game_over = False
state = ""
found_latter = []

for char in your_word:
    word_placeholder += "_ "        

print(word_placeholder)
print(f"\nYou have to guess a word with {len(your_word)} latter")

while not game_over:
    guessed_latter = input("\n\nWrite your guess: ").lower()
    state = ""
    found = False
    found_already = False
    for char in your_word:
        if char == guessed_latter:
            state += guessed_latter
            found = True
            if char not in found_latter:
                found_latter.append(char)                
            else:
                found_already = True
        elif char in found_latter:
            state += char
        else:
            state += "_"
    if found_already:
        print("You already guessed this!")
    if not found:
        lives -= 1
        print(f"You lost a life\nYou have {lives} remaining")
        if lives == 0:
            game_over = True
            print("Game Over\n\n")
            show_ans = input("Wish to know the word? (yes/no)").lower()
            if show_ans == "yes" or show_ans == "y":
                print(f"\n\nYour Word Was: {your_word}\n\n")

    if "_" not in state:
        print("You win!")
        game_over = True