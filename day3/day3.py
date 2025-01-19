# Day 3

rider_height = int(input("Enter you height in cm: "))
rider_age = int(input("Enter you age: "))

if rider_height >= 120 and rider_age > 18:
    print("You can ride the rollercoaster")
else:
    print("You can't ride the rollercoaster")


if rider_height >= 120:
    print("You can ride the rollercoaster")
    if rider_age >= 18:
        print("You have to pay $5")
    else:
        print("You have to pay $3")

else:
    print("You can't ride the rollercoaster")
    

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")


# ELIF Weather

current_temp = int(input("Enter Current temperature: "))

if current_temp < 10:
    print("This is so cold")
elif current_temp < 20:
    print("Weather is nice")
elif current_temp < 30:
    print("Weather is warm")
else:
    print("Weather is hot")


# Condition

user_height = int(input("Enter your height in cm: "))
user_age = int(input("Enter your age: "))
user_photo = input("Do you want to take a photo? (yes / no)")
user_bill = 0

if user_height >= 100:
    print("You can ride the rollercoaster")
    if user_age >= 18:
        print("You have to pay $50 for ride")
        user_bill+=50
    elif user_age >= 12:
        print("You have to pay $30 for ride")
        user_bill+=30
    else:
        print("You have to pay $20 for ride")
        user_bill+=20

    if user_photo == "yes":
        print("You have to pay $3 for photo")
        user_bill+=3
    else:
        print("No photo of you")

    print(f"=========== You have to pay total ${user_bill} ============")
else:
    print("You can't ride the rollercoaster")

#logical operator

number = int(input("Enter a number: "))

if number < 0 and number % 2 == 0:
    print("Number is negative and even")
elif number < 0 or number % 2 == 0:
    print("Number is negative or even")
elif number != 0:
    print("Number is not zero")
else:
    print("Number is positive and odd")


# Make your decision

print('''          _       __     __                        
        | |     / /__  / /________  ____ ___  ___ 
        | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \
        | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/
        |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/                             
''')

print("Welcome To Your Decision Making Game")

group = input("You recently completed JSC and it's time to get your self to the next level. Choose your group (Science, Arts, Commerce)\n").lower()

if group == "science":
    career = input("You are in Science Group, Now you can choose your Future Career (Doctor, Engineer, Lawyer)").lower()
    if career == "doctor":
        print("You are a Doctor")
    elif career == "engineer":
        print("You are an Engineer")
    elif career == "lawyer":
        print("You are a Lawyer")
    else:
        print("Game over --- You have to choose from given option")
elif group == "arts":
    career = input("You are in Arts Group, Now you can choose your Future Career (Actor, Singer, Politician)").lower()
    if career == "actor":
        print("You are an Actor")
    elif career == "singer":
        print("You are a Singer")
    elif career == "politician":
        print("You are a Politician")
    else:
        print("Game over --- You have to choose from given option")
elif group == "commerce":
    career = input("You are in Commerce Group, Now you can choose your Future Career (Accountant, Businessman, Lawyer)").lower()
    if career == "accountant":
        print("You are an Accountant")
    elif career == "businessman":
        print("You are a Businessman")
    elif career == "lawyer":
        print("You are a Lawyer")
    else:
        print("Game over --- You have to choose from given option")
else:
    print("Game over --- You have to choose from given option")

