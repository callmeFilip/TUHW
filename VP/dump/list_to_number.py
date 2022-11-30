numbers_list = [12, 3, 456, 78]
number = 0

# for i in range(len(numbers_list)):
#     numbers_list[i]

str_buff = '0'
for i in range(len(numbers_list)):
    str_buff += str(numbers_list[i])

print(int(str_buff))
