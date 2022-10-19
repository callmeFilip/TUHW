import random

length = int(input())

number_list = []

for index in range(length):
    number_list.append(random.randint(0, 100))

print(min(number_list))
print(max(number_list))
