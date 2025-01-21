import random

capital_later = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
smaller_later = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol_array = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", ",", ".", "/", "<", ">", "?"]

possibilities = [capital_later, smaller_later, number_array, symbol_array]

print("Welcome To Password Generator Python Application\n")

length = int(input("~ Password Length: "))
length_capital = int(input("~ How Many Capital Later: "))
length_small = int(input("~ How Many Smaller Later: "))
length_number = int(input("~ How Many Number: "))
length_symbol = int(input("~ How Many Symbol: "))
combined_length = length_capital + length_small + length_number + length_symbol

row_password = []

print(row_password)

if length != combined_length:
    print(f"You asked for {length} digit password but your total is {combined_length}\n\nExiting Without Generating Password")
else:

    for number in range (0, length_capital+1):
        row_password.append(random.choice(capital_later))

    for number in range (0, length_small+1):
        row_password.append(random.choice(smaller_later))

    for number in range (0, length_number+1):
        row_password.append(random.choice(number_array))

    for number in range (0, length_symbol+1):
        row_password.append(random.choice(symbol_array))

    random.shuffle(row_password)

    print(f"Here Is your random password: {''.join(row_password)}")


    # while length_capital > 0:
    #     row_password.append(random.choice(capital_later))
    #     length_capital = length_capital - 1
    # while length_small > 0:
    #     row_password.append(random.choice(smaller_later))
    #     length_small = length_small - 1
    # while length_number > 0:
    #     row_password.append(random.choice(number_array))
    #     length_number = length_number - 1
    # while length_symbol > 0:
    #     row_password.append(random.choice(symbol_array))
    #     length_symbol = length_symbol - 1

    # random.shuffle(row_password)

    # print(f"Here Is your random password: {''.join(row_password)}")
