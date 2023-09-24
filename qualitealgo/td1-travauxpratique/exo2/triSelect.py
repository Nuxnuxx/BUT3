import random
import timeit
import matplotlib.pyplot as plt

T = [random.randint(1,  500) for _ in range(0, 10)]


def tri_selection(t):
    n = len(t)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if t[j] < t[min_idx]:
                min_idx = j
        if min_idx != i:
            t[i], t[min_idx] = t[min_idx], t[i]


# Pour le meilleur cas (tableau déjà trié dans l'ordre croissant) :
# T_meilleur_cas = list(range(1, 101))
# tri_selection(T_meilleur_cas)
# print("Tableau après tri (meilleur cas) :", T_meilleur_cas)

# Pour le "pire des cas" (tableau trié dans l'ordre décroissant) :
# T_pire_cas = list(range(100, 0, -1))
# tri_selection(T_pire_cas)
# print("Tableau après tri (pire des cas) :", T_pire_cas)

# Programme principal
x, y1 = [], []

for i in range(1, 10000, 100):
    n = [random.randint(1,  500) for _ in range(0, i)]

    t1 = timeit.timeit("tri_selection(n)", globals=globals(), number=1)
    x.append(i)
    y1.append(t1)


# Tracer le graphique
plt.plot(x, y1, marker='o', linestyle='-', color='b', label='prems')
plt.xlabel('Abscisses')
plt.ylabel('Ordonnés')

# Afficher le graphique
plt.savefig("triselect.png")
