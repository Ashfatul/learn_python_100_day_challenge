# list comprehension
# name = "Ashfatul"
# letters = [l + 'a' for l in name]
# print(letters)

# numbers = [1,5,2,3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# numbers = [range(1,5)]
# print(numbers)

# num = [n * 2 for n in range(1,5)]
# print(num)

# num = [n for n in range(2,9) if n % 2]
# print(num)

names = ["dina", "dishant", "disha", "a", "aa"]
upto_four = [name.upper() for name in names if len(name) < 5]
print(upto_four)