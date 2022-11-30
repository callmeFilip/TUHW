# # valuten kalkulator pund evro dolar lev

# first_type = int(input('1 euro\n2 pound\n3 dollar\n4 lev\nChoose: '))

# second_type = int(input('1 euro\n2 pound\n3 dollar\n4 lev\nChoose: '))

# outcome = float(input('Input value: '))

# if first_type == second_type:
#     print(f'{outcome:.2f}')
#     exit(0)

# EURO = 1
# POUND = 2
# DOLLAR = 3
# LEV = 4

# if first_type == EURO:

#     if second_type == POUND:
#         outcome *= 0.86

#     elif second_type == DOLLAR:
#         outcome *= 1.03

#     elif second_type == LEV:
#         outcome *= 1.96

# elif first_type == POUND:

#     if second_type == EURO:
#         outcome *= 1.16

#     elif second_type == DOLLAR:
#         outcome *= 1.20

#     elif second_type == LEV:
#         outcome *= 2.27

# elif first_type == DOLLAR:

#     if second_type == EURO:
#         outcome *= 0.97

#     elif second_type == POUND:
#         outcome *= 0.83

#     elif second_type == LEV:
#         outcome *= 1.89

# elif first_type == LEV:

#     if second_type == EURO:
#         outcome *= 0.51

#     elif second_type == POUND:
#         outcome *= 0.44

#     elif second_type == DOLLAR:
#         outcome *= 0.53

# print(f'{outcome:.2f}')

# # godina i mesec ot klaviaturata i se printira dali ima v tozi mesec ot tazi godina
# # ima ponedelnik koito e 24ti

# from datetime import date

# year, month = [int(x) for x in (input('YYYY/MM: ').split('/'))]
# day = 24

# time = date(year, month, day)

# if time.weekday() == 0:
#     print(True)
# else:
#     print(False)

# # string ot klaviatura i trqbva da se vurnat v konzolata vsichki malki bukvi ot
# # stringa i tehniq broi

# text = input('input text: ')

# count = 0
# for char in text:
#     if ord('a') <= ord(char) and ord(char) <= ord('z'):
#         print(char, end='')
#         count += 1
# print('\nChar count:', count)

# # binaren kum 16tichen kalkulator
# def num_to_hex(number):
#     as_str = ''
#     for i in number:
#         as_str += i

#     if as_str == '0000':
#         return '0'
#     elif as_str == '0001':
#         return '1'
#     elif as_str == '0010':
#         return '2'
#     elif as_str == '0011':
#         return '3'
#     elif as_str == '0100':
#         return '4'
#     elif as_str == '0101':
#         return '5'
#     elif as_str == '0110':
#         return '6'
#     elif as_str == '0111':
#         return '7'
#     elif as_str == '1000':
#         return '8'
#     elif as_str == '1001':
#         return '9'
#     elif as_str == '1010':
#         return 'A'
#     elif as_str == '1011':
#         return 'B'
#     elif as_str == '1100':
#         return 'C'
#     elif as_str == '1101':
#         return 'D'
#     elif as_str == '1110':
#         return 'E'
#     elif as_str == '1111':
#         return 'F'


# bin = list(input('input binary: '))

# GROUP = 4

# zeroes_to_add = GROUP - (len(bin) % GROUP)

# for i in range(zeroes_to_add):
#     bin.insert(0, '0')

# hex_count = len(bin) // GROUP
# for i in range(hex_count):
#     print(num_to_hex(bin[i*4: (i+1)*4]), end='')
# print()

# print(bin)

# # vuvejda se cqlo polojitelno chislo, programata trqbva da nameri koren,
# # v sluchai che ne e cqlo, polojitelno ili e 0 da se vurne greshka

# from math import sqrt

# while True:
#     try:
#         number = int(input('Input integer: '))
#         if number == 0:
#             raise ValueError('value equals 0')

#         print(sqrt(number))
#         break

#     except ValueError as inst:
#         print(
#             f'Value must be an integer, greater than 0!\nError: {inst}')
