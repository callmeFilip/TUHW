year = int(input())

if year % 100 == 0:
    if (year // 100) % 4 == 0:
        print('leap')
    else:
        print('not leap')
else:
    if year % 4 == 0:
        print('leap')
    else:
        print('not leap')
