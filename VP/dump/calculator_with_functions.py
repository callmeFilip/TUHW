# kalkulator za celi chisla, potrebitelq vuvejda funkciqta, posle po 2 chisla
def printMenu():
    print("Operations list:\n"
          "1: +\n"
          "2: -\n"
          "3: *\n"
          "4: /\n"
          "5: exit"
          )


def plus(left, right):
    return left + right


def minus(left, right):
    return left - right


def multiplication(left, right):
    return left * right


def division(left, right):
    return left / right if right != 0 else None


operation = 0

while True:
    printMenu()
    operation = int(input('Input operation: '))

    if operation == 5:
        break

    left = int(input('Input left integer: '))
    right = int(input('Input right integer: '))

    if operation == 1:
        print(plus(left, right))
    elif operation == 2:
        print(minus(left, right))
    elif operation == 3:
        print(multiplication(left, right))
    elif operation == 4:
        print(division(left, right))
    else:
        print('Invalid operation!')
    print('------\n')

print('exiting...')
