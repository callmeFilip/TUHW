# 3
a = int(input('a: '))
b = int(input('b: '))

sum_one = 0
for i in range(a, b + 1):
    sum_one += i

sum_two = 0
i = 0
while a + i <= b:
    sum_two += a + i
    i += 1

print(f'Sumata na chislata ot a do b e = {sum_one}')

print(f'Sumata na chislata ot a do b e = {sum_two}')

# 4
sum_three = 0
while True:
    command = input('Shte vuvejdate li oshte chisla: ')

    if command == 'N':
        break

    sum_three += int(command)

print(f'Sumata na chislata ot a do b e = {sum_three}')

print('Good bye')
