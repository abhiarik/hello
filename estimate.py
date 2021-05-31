import random


def wallis(n):
    pi = 1
    for i in range(1, n+1):
        pi = pi * ((4*i**2)/(4*i**2-1))
    return 2*pi


def monte_carlo(n):
    x = []
    y = []
    d = []
    In_circle = 0
    In_square = 0
    for i in range(n):
        x.append(random.random())
        y.append(random.random())
    for j in range(n):
        d.append((x[j]**2+y[j]**2)**(1/2))
    for k in d:
        if k < 1:
            In_circle += 1
            In_square += 1
        else:
            In_square += 1
    return 4*(In_circle/In_square)
