tableau = list(range(0, 10))


def rechercheSequentielle(x, tab):
    for i in range(1, len(tab)):
        if tab[i] == x:
            return i
    return -1

# Programme principale


test = rechercheSequentielle(1, tableau)
print(test)
