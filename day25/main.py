# with open('data.csv') as data_file:
# 	data = data_file.readlines()

# 	print(data)


# import csv
# from operator import indexOf

# with open('data.csv') as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for item in data:
#         if item[1] == 'temp':
#             continue
#         else:
#             temp.append(int(item[1]))

#     print(temp)

import pandas as pd

data = pd.read_csv('data.csv')
print(data['temp'].to_list())

# average = sum(data['temp']) / len(data['temp'])
# print(average)

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.day[0] == 'Monday') 
# print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])