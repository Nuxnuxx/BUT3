# Ecrire une fonction de partitionnement de la liste L en deux sous-listes L' et L" suivant un
# pivot piv, tel que tous les éléments dans L' sont inférieurs à piv et tous les élément de L" sont
# supérieurs à piv. Cette fonction retournera la position du pivot dans la liste ainsi
# partitionnée.

def partition(L, dev, fin):
    pivot = L[dev]
    i = dev + 1
    j = fin
    while i <= j:
        while i <= j and L[i] <= pivot:
            i = i + 1
        while i <= j and L[j] >= pivot:
            j = j - 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    L[dev], L[j] = L[j], L[dev]
    return j

# B. Quelle est le coût de cette fonction ?

'''Le coût de la fonction de partitionnement dépend du nombre de comparaisons et d'échanges effectués. Dans le pire des cas, la liste est inversée par rapport au pivot, ce qui entraîne n - 1 comparaisons (où n est le nombre d'éléments dans la liste) et n - 1 échanges. Donc, dans le pire des cas, le coût de la fonction de partitionnement est O(n^2).'''

# C. Ecrire l'algorithme récursif du tri rapide faisant appel à cette fonction.

def tri_rapide(L, dev, fin):
    if dev < fin:
        pivot = partition(L, dev, fin)
        tri_rapide(L, dev, pivot - 1)
        tri_rapide(L, pivot + 1, fin)

# D. Définir le cas favorable et le cas défavorable du tri rapide. Illustrez par un schéma.

'''Avant le tri :
[1, 2, 3, 4, 5]

Étape 1 (pivot = 1) :
[1] [2, 3, 4, 5]

Étape 2 (pivot = 2) :
[1] [2] [3, 4, 5]

Étape 3 (pivot = 3) :
[1] [2] [3] [4, 5]

Étape 4 (pivot = 4) :
[1] [2] [3] [4] [5]

Après le tri :
[1, 2, 3, 4, 5]
'''
