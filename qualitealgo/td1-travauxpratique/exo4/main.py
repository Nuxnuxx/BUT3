import random

nombr_element = 5

KNOW = [[random.randint(0, 1) for j in range(nombr_element)] for i in range(nombr_element)]


def know(a, b):
    return KNOW[a-1][b-1] == 1


def wits_first(n, know):
    for i in range(1, n + 1):
        isastar = True
        for j in range(1, n + 1):
            if (i != j) and not know(j, i):
                isastar = False
                break
        for j in range(1, n + 1):
            if (i != j) and know(i, j):
                isastar = False
                break
        if isastar:
            return i
    return 0


def find_star(n, know):
    candidate = 1
    for i in range(2, n + 1):
        if know(candidate, i):
            candidate = i

    # Now, validate if the 'candidate' is actually a star.
    for i in range(1, n + 1):
        if i != candidate:
            if not know(i, candidate) or know(candidate, i):
                return 0

    return candidate


print(find_star(nombr_element, know))
