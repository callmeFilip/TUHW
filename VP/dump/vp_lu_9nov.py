# napishe programa, koqto da sustavi vsichki vuzmojnosti ot x y z o

symbols = ['x', 'y', 'z']

for i in range(len(symbols)):
    for j in range(1, len(symbols)):
        print(symbols[i], end='')
        for k in range(1, len(symbols)):
            print(symbols[k - i + j], end='')
        print()

# funkciq priema v arg spisuk, precenqva dali e monotonno namalqvashta,
# uvelichavashta se posledovatelnost ili neopredeleno
# def check_trend(numbers):
#     if len(numbers) < 2:
#         return 'unindentified'

#     diff = numbers[1] - numbers[0]

#     if diff < 0:
#         # namalqvashta
#         for i in range(len(numbers) - 1):
#             if numbers[i+1] - numbers[i] != diff:
#                 return 'unindentified'
#         return 'decrementing'

#     elif diff > 0:
#         # uvelichavashta
#         for i in range(len(numbers) - 1):
#             if numbers[i+1] - numbers[i] != diff:
#                 return 'unindentified'
#         return 'incrementing'

#     return 'unindentified'


# test = [1]
# print(check_trend(test))


# funkciq priema argument spisuk s 20 elementa (s povtarqshti se)
# i suzdava nov spisuk v koito dobavq sushtite elementi ot purviq spisuk,
# no ostavq samo unikalnite (premahva povtarqshtite se)

# def clean_repeating(dirty):
#     clean = list()
#     for i in dirty:
#         if i not in clean:
#             clean.append(i)
#     return clean


# dirty_list = list()
# for i in range(20):
#     dirty_list.append(i)

# dirty_list[4] = 2
# dirty_list[5] = 2
# dirty_list[6] = 7

# clean_list = clean_repeating(dirty_list)
# print(clean_list)


# funkciq priema kato argument string i presmqta kolko glavni i kolko
# malki bukvi ima i go printira

# from string import ascii_lowercase as lower
# from string import ascii_uppercase as upper


# def count_letters(text):
#     capital_letters = 0
#     small_letters = 0

#     for i in range(len(lower)):
#         small_letters += text.count(lower[i])
#         capital_letters += text.count(upper[i])

#     return capital_letters, small_letters


# text = "asdfghjklASDasd123FGHJK 12345~!@2"
# print(count_letters(text))

# napishete programa na python, koqto obrushta
# podadenoto ot potrebitel 4 cifreno chislo kato
# subira originalnoto schislo s oburnatoto
# i proverqva dali rezultata e palindrom,
# ako ne e palindrom otnovo se
# vuvejda novo chislo, ako e palindrom return

# while True:
#     number = input('Input 4 digits: ')

#     reversed_number = number[::-1]

#     sum = int(number) + int(reversed_number)
#     if str(sum) == str(sum)[::-1]:
#         print(sum)
#         break
