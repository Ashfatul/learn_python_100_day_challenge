# # Rock paper scissors

# import random
# def rock_paper_scissors():
#     print("=================================\nWelcome to Rock, Paper, Scissors\n=================================\n\n")
#     user_input = input("Enter your choice: (rock/r, paper/p, scissors/s): ").lower()

#     if user_input == "r" or user_input == "rock":
#         print("You ~ Rock")
#     elif user_input == "p" or user_input == "paper":
#         print("You ~ Paper")
#     elif user_input == "s" or user_input == "scissors":
#         print("You ~ Scissors")
#     else:
#         print("Invalid input")

#     computer_input = random.choice(["rock", "paper", "scissors"])
#     print("Computer ~ ", computer_input)

#     if user_input == computer_input:
#         print("Draw")
#     elif user_input == "r" or user_input == "rock" and computer_input == "scissors":
#         print("You win -- Rock crushes Scissors")
#     elif user_input == "p" or user_input == "paper" and computer_input == "rock":
#         print("You win -- Paper covers Rock")
#     elif user_input == "s" or user_input == "scissors" and computer_input == "paper":
#         print("You win -- Scissors cuts Paper")
#     else:
#         print("You lose -- Computer Wins")

# while True:
#     rock_paper_scissors()
#     play_again = input("\n\nPlay again? (yes/no): ").lower()
#     if play_again == "n" or play_again == "no":
#         break




# import random
# a = random.randint(1000000000000000000000000,5000000000000000000000000000000000000)
# print(a)

# a = random.random();
# print(a)

import random
list_of_employee = ["Jhon", "Linkon", "Abraham", "Ismail", "Rohim"]
# id = random.randint(0,4)

# print(f"{list_of_employee[id]}, you have been promoted")

user = random.choice(list_of_employee)
print(user)
