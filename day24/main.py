with open("data.txt", mode="a") as data:
    info = data.write("working 99999999999999999999999999")


with open("data.txt") as text:
    print(text.read())