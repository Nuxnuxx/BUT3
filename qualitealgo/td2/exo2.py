import random
import timeit
import matplotlib.pyplot as plt


def rechercheSequentielle(x, tab):
    for i in range(len(tab)):
        if tab[i] == x:
            return i
    return -1


def rechercheDichotomique(x, tab):
    deb, fin = 0, len(tab) - 1
    while deb <= fin:
        mid = (deb + fin) // 2
        if tab[mid] == x:
            return mid
        elif tab[mid] < x:
            deb = mid + 1
        else:
            fin = mid - 1
    return -1


x, y_seq, y_dich = [], [], []

# nombre d'exécutions pour chaque taille pour lisser les temps
num_runs = 10

for i in range(1, 10000, 100):
    T = list(range(i))
    target = random.choice(T)

    # Calcul des temps moyens sur plusieurs exécutions
    t_seq = sum(timeit.timeit(lambda: rechercheSequentielle(
        target, T), number=1) for _ in range(num_runs)) / num_runs
    t_dich = sum(timeit.timeit(lambda: rechercheDichotomique(
        target, T), number=1) for _ in range(num_runs)) / num_runs

    x.append(i)
    y_seq.append(t_seq)
    y_dich.append(t_dich)

plt.figure(figsize=(10, 6))
plt.plot(x, y_seq, '-b', label='Recherche Séquentielle')
plt.plot(x, y_dich, '-r', label='Recherche Dichotomique')
plt.xlabel('Taille du tableau')
plt.ylabel('Temps d\'exécution (s)')
plt.legend()
plt.grid(True)
plt.show()
