import numpy as np
import matplotlib.pyplot as plt

with open('ExpModifiee.txt', 'r', encoding='utf-8') as f:
    y_points = [float(line.strip()) for line in f]

x = np.linspace(0, 0.2, 201)

point = input("")
point = int(point)
t = np.log(y_points[point])/x[point]
print(t, y_points[point], x[point])
a = y_points[point]/np.exp(t*x)
y_gauss = a*np.exp(t*x)

plt.style.use("grayscale")

plt.plot(x, y_gauss, label='Gausienne')

plt.scatter(x, y_points, color='red',
            marker='o', label='ExpModifie.txt')

plt.title("test")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("exponential_curve.png")
