def printMenu():
    print("Input operation:\n"
        "1: +\n"
        "2: -\n"
        "3: *\n"
        "4: /\n"
        "5: exit"
        )


while True:
    number1 = int(input('First number: '))
    number2 = int(input('Second number: '))
    printMenu()

    operation = int(input())

    if operation == 1:
        print(number1 + number2)
    
    elif operation==2:
        print(number1 - number2)
    
    elif operation==3:
        print(number1 * number2)
    
    elif operation==4:
        print(number1 / number2)
    
    elif operation==5:
        break
    
    else:
        print('Invalid operation!')

print("---")