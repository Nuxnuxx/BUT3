'''
    realiser un simulateur d'un bras robotique compose de deux elements :
        E1 = 50cm
        E2 = 20cm

E1 et E2 effectuent des rotations dans le meme XY

Ecrirer un programme qui :

-> prend en entree 01 et 02

-> calcule les coordonnees de la pince (extremite de E2)

-> affiche ces 2 coordonnees

-> affiche le robot a cette configuration
'''
import math
import numpy as np
import matplotlib.pyplot as plt

o1 = input('rotation numero 1: ')
o2 = input('rotation numero 2: ')

E1 = 50
E2 = 20

theta1 = math.radians(float(o1))
theta2 = math.radians(float(o2))

# calcule les coordonnes de la pince
P = [E1*math.cos(theta1)+E2*math.cos(theta1+theta2), E1*math.sin(theta1)+E2*math.sin(theta1+theta2)]

print('les coordonnes de la pince sont: ', P)


start_point = np.array([[0, 0], [E1 * math.cos(theta1), E1 * math.sin(theta1)], P])

end_point = np.array([[E1 * math.cos(theta1), E1 * math.sin(theta1)], P, P])

fig,ax = plt.subplots()

for start , end in zip(start_point, end_point):
    ax.plot([start[0], end[0]], [start[1], end[1]], 'k-', lw=2)


ax.plot(start_point[:,0], start_point[:,1], 'ro')

ax.plot(end_point[:,0], end_point[:,1], 'bo')

ax.plot (P[0], P[1], 'go')

ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
ax.set_aspect('equal', adjustable='box')
plt.grid()

plt.savefig('robot.png')
