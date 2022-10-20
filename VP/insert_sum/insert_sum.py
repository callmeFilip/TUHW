import random
numbers = []

for index in range(5):
    numbers.append(random.randint(0, 10))

print(numbers)

result_list = []

for i in range(len(numbers) - 1):
    result_list.append(numbers[i])
    result_list.append(numbers[i] + numbers[i+1])

result_list.append(numbers[-1])

print(result_list)
