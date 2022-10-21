import random

# init
LIST_SIZE = 10
numbers = []


# fill list
for i in range(LIST_SIZE):
    numbers.append(random.randint(100, 999))

print(list)


# find and sum
sum = 0
for number in numbers:
    if (number // 100 + ((number) // 10) % 10 + number % 10) % 2 != 0:
        sum += number


print(sum)
