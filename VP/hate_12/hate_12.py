import random

numbers = []

for index in range(20):
    numbers.append(random.randint(0, 100))

print(numbers)

print('[', end='')
for i in range(len(numbers) - 1):
    if numbers[i] == 12:
        continue
    print(numbers[i], end=', ')
print(str(numbers[-1]) + ']')
