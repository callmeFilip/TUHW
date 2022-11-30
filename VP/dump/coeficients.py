a = int(input('a: '))
b = int(input('b: '))
x = 0
if a == 0:
    if b == 0:
        print('Every x')
    else:
        print('None')
else:
    x = -b/a
    print(x)
