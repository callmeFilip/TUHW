from random import choice
from string import ascii_lowercase

n = int(input('input n: '))

text_list = []

for _ in range(n):
    text_list.append(choice(ascii_lowercase))
print(text_list)


text_tuple = tuple(text_list)
print(text_tuple)

# 1
text_set = set(text_tuple)
print(text_set)
# 2
tuple_list = []
for i in text_set:
    print(f'{i} is seen {text_tuple.count(i)} times')
    # 3
    each_char_tuple = (i, text_tuple.count(i))
    # 4
    tuple_list.append(each_char_tuple)

print(tuple_list)

# 5
list_dict = dict()
for el in tuple_list:
    list_dict[el[0]] = el[1]

print(list_dict)
