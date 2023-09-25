tableau = list(range(0, 10))


def rechercheSequentielle(x, tab):
    for i in range(1, len(tab)):
        if tab[i] == x:
            return i
    return -1

# Programme principale


test = rechercheSequentielle(1, tableau)
print(test)

# Pour le "meilleur des cas" (tableau trié dans l'ordre décroissant) :
T_meilleur_cas = list(range(1, 101))
i = rechercheSequentielle(1, T_meilleur_cas)
print(i)

# Pour le "pire des cas" (tableau trié dans l'ordre décroissant) :
T_pire_cas = list(range(100, 0, -1))
i = rechercheSequentielle(101, T_pire_cas)
print(i)
