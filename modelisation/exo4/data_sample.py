import numpy as np
import matplotlib.pyplot as plt

with open('./ExpBruitee.txt', 'r', encoding='utf-8') as f:
    y = [float(line.strip()) for line in f]

x = np.linspace(0, 2, len(y))
a = np.array([[xi, 1] for xi in x])
b = np.array([[np.log(yi)] for yi in y])

at = np.transpose(a)

X = np.linalg.inv(at @ a) @ at @ b

y = X[0]*x + X[1]

plt.plot(x, y, label="Moindre carre ExpBruitee")

plt.title("Moindre carre ExpBruitee")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("test.png")
