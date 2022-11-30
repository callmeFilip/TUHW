# def fun(container):
#     result = [container[0], 0]

#     for i in range(1, len(container)):
#         if container[i] > result[0]:
#             result[0] = container[i]
#             result[1] = i

#     return result


# numbers = [1, 0, 2, 8, 0, 8]

# print(fun(numbers))


##


# def add(*numbers):
#     return sum(numbers)


# def multiply(*numbers):
#     result = 0
#     if numbers:
#         result = 1
#         for num in numbers:
#             result *= num
#     return result


# def main(operation='op+', chisla=(3, 2)):
#     if operation == 'op+':
#         print(add(*chisla))
#     else:
#         print(multiply(*chisla))
#     print('op =', operation)
#     return None


# main()
# main('op*')
# main(chisla=(2, 4, 3), operation='op*')

from math import sqrt as squared


class vector:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return squared(self.x**2 + self.y**2 + self.z**2)


vectorA = vector('Vector A', 3, 4, 5)
vectorB = vector('Vector B', 3, 5, 4)

A = vectorA.norm()
B = vectorB.norm()


print(A)
print(B)


class scalar(vector):
    def scararproduct():
        pass
