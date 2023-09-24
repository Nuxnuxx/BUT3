import timeit
import matplotlib.pyplot as plt


# définition d'une fonction
def somme(n):
    total = 0
    for i in range(1, n+1):
        total *= i
    return total


# Programme principal
x, y1, y2 = [], [], []

for i in range(1, 1000, 100):
    n = i
    t1 = timeit.timeit("somme(n)", globals=globals(), number=1)
    t2 = timeit.timeit("somme(n)", globals=globals(), number=100)
    x.append(i)
    y1.append(t1)
    y2.append(t2)

# Tracer le graphique
plt.plot(x, y1, marker='o', linestyle='-', color='b', label='prems')
plt.plot(x, y2, marker='*', linestyle='-', color='r', label='deuze')
plt.xlabel('Abscisses')
plt.ylabel('Ordonnés')

# Afficher le graphique
plt.savefig("d.png")
