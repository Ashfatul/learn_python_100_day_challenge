# # print(1212)

# # print(3.14566)

# # print(True)

# # print("Hello World")

# # print("Hello World"[0])

# # print("Hello World"[0:2])


# # number = 123456789

# # print("Length of number is : " , len(str(number)), type(number))

# # int_number = 1234
# # float_number = 3.15154
# # name = "John"
# # isRaining = False

# # print(type(int_number))
# # print(type(float_number))
# # print(type(name))
# # print(type(isRaining))

# # # type conversion
# # # int()
# # # float()
# # # str()
# # # bool()

# # print(10+20)
# # print(20-10)
# # print(10*20)
# # print(20/10)
# # print(20%10) # modulus
# # print(20//10) # floor division
# # print(2**3) # 2 to the power of 3

# # print(3+3-6*2/6*4-6)


# # BMI Calculator

# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kg: "))

# print("Your BMI is: ", round((weight/(height**2)), 2))


# print(f"Your BMI is: {round((weight/(height**2)), 2)}") #f string is like template literal in javascript




# Practice tip calculator

print("Calculate how much you have to pay")
cost = input("Your total cost: ")
tip = input("Tip percentage: ")
person = input("Number of people: ")

final_cost = float(cost) + float(cost) * float(tip)/100
each_cost = final_cost/int(person)


print("=============================================================")
print(f"You are {person} people\nYour total cost without tip : {cost}\nYou want to pay {tip}% tip\nYour total cost with tip : {final_cost}")
print("=============================================================")
print(f"Each person should pay: {round(each_cost, 2)}")
