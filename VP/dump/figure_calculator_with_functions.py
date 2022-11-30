# kalkulator za lice i parametur na figura, potrebitelq vuvejda funkciqta,
# posle po n chisla 1: kvadrat 2: pravoufulnik 3: triugulnik 4: okrujnost
import math

from more_itertools import first


def printMenu():
    print("Operations list:\n"
          "1: square\n"
          "2: rectangle\n"
          "3: triangle\n"
          "4: circle\n"
          "5: exit"
          )


def square_area(side):
    return side * side


def square_perimeter(side):
    return 4 * side


def rectangle_area(width, height):
    return width * height


def rectangle_perimeter(width, height):
    return 2 * (width + height)


def triangle_area(first_side, second_side, third_side):
    p = (first_side + second_side + third_side) / 2
    return math.sqrt(p * (p - first_side) * (p - second_side) * (p - third_side))


def triangle_perimeter(first_side, second_side, third_side):
    return first_side + second_side + third_side


def circle_area(radius):
    return math.pi * radius * radius


def circle_perimeter(radius):
    return math.pi * radius * 2


operation = 0

while True:
    printMenu()
    operation = int(input('Input operation: '))

    if operation == 5:
        break

    if operation == 1:
        side = int(input('Input square side: '))
        print(f'S = {square_area(side):.2f}, P = {square_perimeter(side):.2f}')
    elif operation == 2:
        height = int(input('Input rectangle height: '))
        width = int(input('Input rectangle width: '))
        print(
            f'S = {rectangle_area(width, height):.2f}, P = {rectangle_perimeter(width, height):.2f}')
    elif operation == 3:
        first_side = int(input('Input triangle first side: '))
        second_side = int(input('Input triangle second side: '))
        third_side = int(input('Input triangle third side: '))
        print(
            f'S = {triangle_area(first_side, second_side, third_side):.2f}, '
            f'P = {triangle_perimeter(first_side, second_side, third_side):.2f}')
    elif operation == 4:
        radius = int(input('Input circle radius: '))
        print(
            f'S = {circle_area(radius):.2f}, P = {circle_perimeter(radius):.2f}')
    else:
        print('Invalid operation!')

    print('------\n')

print('exiting...')
