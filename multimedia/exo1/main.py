import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 0.2, 1000)
x_2 = np.linspace(0, 0.2, 100)
x_3 = np.linspace(0, 0.2, 10)

A = 220
f = 50
phi = 0
y = A*np.sin(2*np.pi*f*x+phi)
y_2 = A*np.sin(2*np.pi*f*x_2+phi)
y_3 = A*np.sin(2*np.pi*f*x_3+phi)

plt.style.use("grayscale")

plt.plot(x, y, label='fonction sinus generaliser')
plt.plot(x_2, y_2,  color="red")
plt.plot(x_3, y_3, color="blue")

plt.title("test")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("sinus.png")
