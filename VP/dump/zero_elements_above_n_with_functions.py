# funkciq, 2 argumenta, spisuk s chisla i chislo n, vrushta
# rezultat (za n, vsichko po-golqmo ot n v spisuka stava 0)

def func(container, number):
    for i in range(len(container)):
        if container[i] > number:
            container[i] = 0


numbers = [1, 2, 3, 4, 5]
func(numbers, 3)
print(numbers)
