# a = [1, 1, 3, 3, 2]
# b = [3, 4]

# c = tuple()


# d = dict()
# d1 = {'key2': 'value',
#       'key1': 'value 2'}


# print(sorted(d1.keys()))
# print(sorted(d1.keys(), reverse=True))


# print(d1['key2'])


# del d1['key1']
# print(d1)


# s = set(a)
# print(set(a) | set(b))
# print(s)


# functions

# def f(qty, item, price):
#     print(f'{qty} {item} costs {price:.2f}$')


# f(6, 'pears', 2.30)
# f(item='apples', qty=6, price=2.30)


# vuvejdame simvoli
# dict: key-> vsqka bukva, value-> broi sreshtana bukva

# text = input('input text: ')
# dictionary = dict()
# for sym in text:
#     if sym in dictionary:
#         dictionary[sym] += 1
#     else:
#         dictionary[sym] = 1

# print(dictionary)


# vuvejdame cqlo chislo n
# suzdavame spisuk ot 1 do n
# suzdavame dictionary, keys=>elementite ot spisuka, values=>stoinostite, no v obraten red

elements = dict()

# Solution 1:
keys = [i for i in range(1, int(input('Input number: ')) + 1)]

for i in keys:
    elements[i] = keys[-i]

# Solution 2 (Wrong, but right):
# number = int(input('Input number: '))

# for i in range(number):
#     elements[i + 1] = number - i

print(elements)
