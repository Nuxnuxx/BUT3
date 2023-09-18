import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1, 100)

A = 1
f = 200
phi = 0
y = A*np.sin(2*np.pi*f*x+phi)

A2 = 1
f2 = 200
phi2 = np.pi / 2
y_2 = A2*np.sin(2*np.pi*f2*x+phi2)

y_3 = y + y_2

print(y)
print(y_2)

print(y_3)

plt.style.use("grayscale")

# plt.plot(x, y, label='fonction sinus generaliser')
# plt.plot(x, y_2,  color="red")
plt.plot(x, y_3,  color="blue")

plt.title("test")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("sinus.png")
