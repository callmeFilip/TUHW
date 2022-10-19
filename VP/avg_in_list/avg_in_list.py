import math

numbers = [1, 1, 2, 2, 5, 7, 23]

median_element = 0

if len(numbers) % 2 == 0:
    median_index = len(numbers) / 2
    median_element = (numbers[median_index] + numbers[median_index - 1]) / 2
else:
    median_index = len(numbers) / 2
    median_element = numbers[math.floor(median_index)]

if(median_element%2 == 0 or median_element%3 == 0 or median_element%5 == 0 or median_element%7==0) and \
    (median_element != 2 and median_element!= 3 and median_element != 5 and median_element!= 7):
    print("complex")
else:
    print("primary")
