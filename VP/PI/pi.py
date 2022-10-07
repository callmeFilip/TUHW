def find_pi(term):
    pi = 3
    term = (term * 2) + 1
    for i in range(2, term, 2):
        if (i/2)%2 == 0:
            pi -= 4/(i*(i+1)*(i+2))
        else:
            pi += 4/(i*(i+1)*(i+2))
    return pi


print(find_pi(int(input())))
