x = int(input('x: '))
n = int(input('n: '))

# a)
sum_one = 0
for i in range(n + 1):
    sum_one += x**i

print(f'Sumata na chislata ot redicata e {sum_one}')

sum_two = 0
i = 0
while i <= n:
    sum_two += x**i
    i += 1

print(f'Sumata na chislata ot redicata e {sum_two}')

# b)
prev_element = 1
sum_three = 1

if n > 0:
    for _ in range(1, n+1):
        curr_element = prev_element * x
        sum_three += curr_element
        prev_element = curr_element


print(f'Sumata na chislata ot redicata e {sum_three}')
