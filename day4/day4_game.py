import random
choices = ['rock', 'paper', 'scissors']

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''



def play():
    print("=====================================")
    print("Welcome to Rock Scissors Paper Game")
    print("You are playing against Computer")
    print("=====================================")
    print("\n\n\n Pick Your Choice (rock / r, paper / p, scissors / s)\n\n\n")
    

    def get_user_move():
        user_move = input("~ Your Call: ").lower()
        if user_move == "rock" or user_move == "r":
            print(rock)
            user_move = "rock"
            return user_move
        elif user_move == "scissors" or user_move == "s":
            print(scissors)
            user_move = "scissors"
            return user_move
        elif user_move == "paper" or user_move == "p":
            print(paper)
            user_move = "paper"
            return user_move
        else:
            print("Wrong move \n Try again")
            get_user_move()

    user_move = get_user_move()

    computer_move = random.choice(choices)

    if computer_move == "rock":
        print("~ Computer Call: rock")
        print(rock)
    elif computer_move == "paper":
        print("~ Computer Call: paper")
        print(paper)
    else:
        print("~ Computer Call: scissors")
        print(scissors)

    print("======== Game Result Is ==========")
    if user_move == computer_move:
        print("This is a draw")
    elif user_move == "rock" and computer_move == "scissors":
        print ("You are a Winner")
    elif user_move == "paper" and computer_move == "rock":
        print ("You are a Winner")
    elif user_move == "scissors" and computer_move == "paper":
        print ("You are a Winner")
    else:
        print("You are a looser!")    
    print("======== The End =========")
    


while True:
    play()
    play_again = input("\n\n\Play Again? yes/no (y/n): ").lower()
    if play_again not in ["yes", "y"]:
        print("Ending Game ....")
        break