# vuvejdame data, printira se den ot sedmicata date, time
# from datetime import date

# date_inp_list = input('input in DD/MM/YYYY format: ').split('/')

# day, month, year = [int(el) for el in date_inp_list]

# date_obj = date(day=day, month=month, year=year)

# if date_obj.weekday() == 0:
#     print('Monday')
# elif date_obj.weekday() == 1:
#     print('Tuesday')
# elif date_obj.weekday() == 2:
#     print('Wednesday')
# elif date_obj.weekday() == 3:
#     print('Thursday')
# elif date_obj.weekday() == 4:
#     print('Friday')
# elif date_obj.weekday() == 5:
#     print('Saturday')
# elif date_obj.weekday() == 6:
#     print('Sunday')


# vuvejdame data, printira se sedmica ot godinata
# from datetime import date

# date_inp_list = input('input in DD/MM/YYYY format: ').split('/')

# day, month, year = [int(el) for el in date_inp_list]

# date_obj = date(day=day, month=month, year=year).isocalendar()

# print(date_obj.week)

# napishete programa, koqto otkriva vsichki godini mejdu 3000 i 4150ta,
# v koito 25ti dekemvri e nedelq
# from datetime import date

# starting_year = 3000
# ending_including_year = 4150

# for i in range(starting_year, ending_including_year + 1):
#     current_date = date(day=25, month=12, year=i)  # 25th, December
#     if current_date.weekday() == 5:
#         print(current_date.year)

# potrebitel vuvejda godina, programata presmqta dali godinata e
# visokosna i go printira
# date_input_list = input('input in DD/MM/YYYY format: ').split('/')

# day, month, year = [int(el) for el in date_input_list]

# if (year % 400 == 0) and (year % 100 == 0):
#     print(f'{year} is leap')
# elif (year % 4 == 0) and (year % 100 != 0):
#     print(f'{year} is leap')
# else:
#     print(f'{year} is not leap')

# napishete programa, koqto suzdava nai-blizkiq palindrom na duma vuvedena
# ot potrebitelq
# import math
# a = input()
# firs_part = ""
# end_result = ""
# if len(a) % 2 == 0:
#     for i in range(0, int(len(a)/2)):
#         firs_part += a[i]
#     end_result += firs_part
#     end_result += firs_part[::-1]

# else:
#     for i in range(0, math.floor(len(a)/2)):
#         firs_part += a[i]
#     end_result += firs_part
#     end_result += a[i+1]
#     end_result += firs_part[::-1]
# print(end_result)

# from math import ceil


# def is_palindrome(word):
#     return True if word[::-1] == word else False

# def fix_word(word):
#     result = ''
#     temp_list = list(word)

#     word_range = ceil(len(word) / 2)
#     # word_range = len(word)

#     for i in range(word_range):
#         if word[i] != word[-1 - i]:
#             temp_list[-1 - i] = word[i]

#     for el in temp_list:
#         result += el

#     return result


# original = input('word: ')

# if is_palindrome(original):
#     print(original)
# else:
#     print(fix_word(original))


# napishete programa, koqto namira vsichki chisla, po-golemi ot
# 18 i vtora cifra chetno chislo, izborut stava ot spisuk, kato spisuka
# se obrazuva ot 1 do n prez 3, kato n e 3cifreno chislo ot potrebitel
# n = int(input('Input n: '))

# container = []

# for i in range(1, n, 3):
#     container.append(i)

# for i in range(6, len(container)):
#     if container[i] < 100:
#         if (container[i] % 10) % 2 == 0:
#             print(container[i])
#     else:
#         if ((container[i] // 10) % 10) % 2 == 0:
#             print(container[i])


# potrebitel vuvejda radiani, programata printira gradusi

# def rad_deg(rad):
#     return rad * 180


# def deg_rad(deg):
#     return deg / 180


# choice = int(input('1 - rad -> deg\n2 - deg -> rad\n'))

# val = int(input('value: '))

# if choice == 1:
#     print(rad_deg(val))
# if choice == 2:
#     print(deg_rad(val))


# potrebitel vuvejda text ot consolata, texta se sustoi
# ot bukvi i prazni mesta. Programata printira
# dve dumi v konzolata, ednata e nai-chesto sreshtanata
# a vtorata duma e nai-dulgata

#    NE E RESHENA!

# txt = input('Input text: ')

# words = txt.split(' ')

# dict_keys = set(words)

# words_dict = {}

# for key in dict_keys:
#     words_dict[key] = 0

# for i in words:
#     words_dict[i] += 1

# longest word
# # init
# longest = len(dict_keys)
# longest_words = [dict_keys[0]]

# for word in dict_keys:
#     current_len = len(word)
#     if longest < current_len:
#         # if we find longer than current longest
#         longest = current_len
#         longest_words = []  # dump current longest
#         longest_words.append(word)  # add as first longest word
#     elif longest == current_len:
#         # if we find as long as the longest
#         longest_words.append(word)  # add as another longest word


# print(longest_words)
