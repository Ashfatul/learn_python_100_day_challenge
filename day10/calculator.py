def plus(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mal(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

calc = {
    "+": plus,
    "-": sub,
    "*": mal,
    "/": div
}
keep_previous = False
result = 0

def calculate(keep_previous, result):
    if keep_previous:
        num1 = result
    else:
        num1 = float(input("Write First Number: "))
    
    op = str(input("Write the operation symbol( +, -, *, /)\nOparetion symbol: "))
    num2 = float(input("Write Second Number: "))

    result = calc[op](num1, num2)
    print(f"Your result is: {num1} {op} {num2} = {result}")

    continue_with_previous = input("Continue with this result ot start new\nType y/n: ").lower()

    if continue_with_previous == 'yes' or continue_with_previous == 'y':
        print("continuing with previous value")
        calculate(True, result)
    else:
        result = 0
        print("starting new")
        calculate(False, result)

calculate(keep_previous, result)