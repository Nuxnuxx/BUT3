import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [6, 11, 10, 15, 20, 18, 22, 25, 28, 26]

# a = np.array([[x[0], 1],[x[1], 1], [x[2], 1], [x[3], 1], [x[4], 1], [x[5], 1], [x[6], 1], [x[7], 1], [x[8], 1], [x[9], 1]])
# b = np.array([[y[0]], [y[1]], [y[2]], [y[3]], [y[4]], [y[5]], [y[6]], [y[7]], [y[8]], [y[9]]])

x = np.linspace(0, 20, len(y))
a = np.array([[xi, 1] for xi in x])
b = np.array([[yi] for yi in y])

at = np.transpose(a)

X = np.linalg.inv(at @ a) @ at @ b

y = X[0]*x + X[1]

plt.plot(x, y, label="test")

plt.title("test")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("test.png")
