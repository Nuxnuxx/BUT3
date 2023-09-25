import timeit
import matplotlib.pyplot as plt
import random

T = [random.randint(-500,  500) for _ in range(0, 100)]


def rechMax(T):
    a = T[0]
    count_test = 0
    for i in range(1, len(T)):
        if T[i] > a:
            count_test += 1
            a = T[i]
    return count_test, a


# Programme principal

T_meilleur_cas = list(range(1, 101))
count, max = rechMax(T_meilleur_cas)
print("Max Best Case :", max, "number of test", count)

T_pire_cas = list(range(100, 0, -1))
rechMax(T_pire_cas)
print("Max Worst Case :", max, "number of test", count)

# Programme principal
x, y1 = [], []

for i in range(1, 10000, 100):
    n = [random.randint(-500,  500) for _ in range(0, i)]

    t1 = timeit.timeit("rechMax(n)", globals=globals(), number=1)
    x.append(i)
    y1.append(t1)


# Tracer le graphique
plt.plot(x, y1, marker='o', linestyle='-', color='b', label='prems')
plt.xlabel('Abscisses')
plt.ylabel('Ordonnés')

# Afficher le graphique
plt.savefig("triselect.png")
