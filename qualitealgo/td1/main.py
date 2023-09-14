import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 50, 50)

y = 10**10 * x**3
y_2 = 2**x

# plt.style.use("grayscale")

plt.plot(x, y, label='10**10 * x**3', color='red')
plt.plot(x, y_2, label='2**n', color='blue')

plt.title("10**10 * x**3 vs 2**n")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("algo.png")
