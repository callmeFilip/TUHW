# if else i elif
# buro za prodajba na bileti, vseki chovek kupuva bileti,
# ot 1 godina do 5 godini putuva bezplatno,
# ot 5 do 10 s 50% namalenie, nad 10 100% ot 10 lv

# cost_per_passanger = 10

# while True:
#     age = input('Input age: ')

#     if age == 'exit':
#         break

#     age = int(age)

#     print('Costs: ', end='')
#     if 0 <= age and age < 5:
#         print(f'{0:.2f}')
#     elif 5 <= age and age <= 10:
#         print(f'{(cost_per_passanger * 0.50):.2f}')
#     else:
#         print(f'{cost_per_passanger}')


# print chislata ot 1 do 20
# prez 2 otzad napred

# for i in range(20, 0, -2):
#     if i != 10:
#         print(i)
# from string import ascii_lowercase as small_letters
# print(small_letters)

# for i in range(ord('a'), ord('z') + 1):
#     print(chr(i))

# sin jult cheven
# words = ["blue", "yellow", "red"]

# for i in words:
#     print(f'{i} \u261b {len(i)}')

# n na broi chisla, ngs
# num = int(input('n: '))

# container = []
# for i in range(num):
#     container.append(int(input('input number: ')))

# min = container[0]
# for i in range(1, num):
#     if i < min:
#         min = container[i]

# print(min)

# num = int(input('n: '))

# total_sum = 0
# for i in range(num):
#     total_sum += int(input('input number: '))

# print(total_sum)

n = int(input('input n: '))

for i in range(1, n + 1):
    print(i * '*')
