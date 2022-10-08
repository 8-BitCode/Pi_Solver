from math import sqrt

pi = 0
x = -1
for y in range(1, 10000000000):
    x = x+2
    if (y % 2) == 0:
        pi = pi - 4/x
    else:
        pi = pi + 4/x

    print(pi)
