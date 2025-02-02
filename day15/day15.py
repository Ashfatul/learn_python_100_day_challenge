# Coffee Machine

import menu
import time
machine_off = False
machine_res = {
                "water": 1000,
                "milk": 500,
                "coffee": 200
              }
machine_balance = 0
machine_coin = {
    "1tk Coin": 1,
    "2tk Coin": 2,
    "5tk Coin": 5
}

def check_recourses(name):
    enough_res = True
    coffee = menu.coffee_menu[name]["resources"]

    for item in coffee:
        if  not (machine_res[item] >= coffee[item]):
            print(f"Not Enough {item}")
            enough_res = False
    
    return enough_res
            

def ask_for_money(command, prepaid = 0):
    print(f"Your coffee will cost {menu.coffee_menu[command]["price"]} BDT\nWe accept 1tk/2tk/5tk Coin\nAdd Quantity of each coin below")
    money = 0
    if prepaid > 0:
        money += prepaid

    for coin in machine_coin:
        try:
            money += int(input(f"Count of {coin}: ")) * machine_coin[coin]
        except:
            print("ERROR: Write a numeric value")
            money += int(input(f"Count of {coin}: ")) * machine_coin[coin]
    return money

def return_money(command, cost, paid):
    ready_to_make_coffee = False
    if paid > cost:
        print(f"Here is your extra {paid - cost} tk return")
        ready_to_make_coffee = True
    elif paid < cost:
        print(f"Not enough Money, You need to add {cost - paid} tk more")
        prepaid = cost - paid
        ask_for_money(command, prepaid)
    elif paid == cost:
        ready_to_make_coffee = True

    return ready_to_make_coffee

def serve_coffee(command):
    print("Preparing your coffee\nPlease Wait 3s ...")
    for res in menu.coffee_menu[command]["resources"]:
        machine_res[res] -= menu.coffee_menu[command]["resources"][res]
    time.sleep(3)
    print(f"Here is your {command}! enjoy\n\nThanks for using Digital Coffee Maker!")
    time.sleep(1)
    print("Making Machine Ready for next order! Just a moment!")
    time.sleep(2)
    print("\n" * 100)



while not machine_off:
    print("===========================")
    print("Welcome To coffee machine")
    print("===========================")
    print("What coffee would like to have?\n")

    for item in menu.coffee_menu:
        print(item)

    command = input("\nChoose Your Coffee: ").lower()

    if command == "off":
        print("Turning of machine ...")
        machine_off = True
    elif command == "status":
        print("Current Recourses of Machine: \n")
        for item in machine_res:
            print(f"{item}: {machine_res[item]}")
        print("\n" * 10)
    elif command == "add":
        print("Add Recourses to machine: ")
        for item in machine_res:
            try:
                machine_res[item] += int(input(f"Add {item}: "))
                print(f"Added recourses")
            except:
                print("ERROR: Write in numeric value")
                machine_res[item] += int(input(f"Add {item}: "))
        print("\n" * 10)
    elif command == "espresso":
        enough_res = check_recourses(command)
        if enough_res:
            print("Coffee can be make")
            paid_money = ask_for_money(command)

            if paid_money > 0:
                make_coffee = return_money(command ,menu.coffee_menu[command]["price"] ,paid_money)

                if make_coffee:
                    machine_balance += menu.coffee_menu[command]["price"]
                    serve_coffee(command)

        else:
            print("Not Enough Recourses")

    elif command == "americano":
        enough_res = check_recourses(command)
        if enough_res:
            print("Coffee can be make")
            paid_money = ask_for_money(command)

            if paid_money > 0:
                make_coffee = return_money(command ,menu.coffee_menu[command]["price"] ,paid_money)

                if make_coffee:
                    machine_balance += menu.coffee_menu[command]["price"]
                    serve_coffee(command)
        else:
            print("Not Enough Recourses")
    elif command == "latte":
        enough_res = check_recourses(command)
        if enough_res:
            print("Coffee can be make")
            paid_money = ask_for_money(command)

            if paid_money > 0:
                make_coffee = return_money(command ,menu.coffee_menu[command]["price"] ,paid_money)

                if make_coffee:
                    machine_balance += menu.coffee_menu[command]["price"]
                    serve_coffee(command)

    elif command == "cappuccino":
        enough_res = check_recourses(command)
        if enough_res:
            print("Coffee can be make")
            paid_money = ask_for_money(command)

            if paid_money > 0:
                make_coffee = return_money(command ,menu.coffee_menu[command]["price"] ,paid_money)

                if make_coffee:
                    machine_balance += menu.coffee_menu[command]["price"]
                    serve_coffee(command)
        else:
            print("Not Enough Recourses")
    elif command == "money":
        print(f"Your machine have {machine_balance} BDT")
    else:
        print("\n\n\nCommand Undefined\n\n\n")
