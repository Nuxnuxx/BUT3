import timeit

# définition d'une fonction


def algo_1(n):
    x = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = 2 ** 4
    return x


def algo_2(n):
    x = 0
    for i in range(n):
        for j in range(1, i+1):
            x = 2 ** 4
    return x


def algo_3(n):
    x = 0
    for i in range(5, n-4):
        for j in range(i-5, i+6):
            x = 2 ** 4
    return x


def algo_4(n):
    x = 0
    for i in range(n):
        for j in range(i):
            for k in range(j):
                x = 2 ** 4
    return x


# Programme principal


n = 100
t1 = timeit.timeit("algo_1(n)", globals=globals(), number=n)
t2 = timeit.timeit("algo_2(n)", globals=globals(), number=n)
t3 = timeit.timeit("algo_3(n)", globals=globals(), number=n)
t4 = timeit.timeit("algo_4(n)", globals=globals(), number=n)

print("t1 = ", t1)
print("t2 = ", t2)
print("t3 = ", t3)
print("t4 = ", t4)
