import math
import numpy as np
import matplotlib.pyplot as plt


E1 = 50
E2 = 20

# ancien programme
o1 =  90
o2 = 0
thetaBon1 = math.radians(float(o1))
thetaBon2 = math.radians(float(o2))
print("theta qui est bon: ",thetaBon1,thetaBon2)

# calcule les coordonnes de la pince
P = [E1*math.cos(thetaBon1)+E2*math.cos(thetaBon1+thetaBon2), E1*math.sin(thetaBon1)+E2*math.sin(thetaBon1+thetaBon2)]
bon_x = P[0]
bon_y = P[1]
print("bon_x",bon_x,"bon_y",bon_y)
# fin ancien programme
thetaResultat1 = np.pi / 2
thetaResultat2 = 0
 
f1 = [E1*math.cos(thetaResultat1)+E2*math.cos(thetaResultat1+thetaResultat2), E1*math.sin(thetaResultat1)+E2*math.sin(thetaResultat1+thetaResultat2)]

for i in range(1,10):
    dfdx = np.array([
        [E1 * -math.sin(thetaResultat1) - E2 * -math.sin(thetaResultat1 + thetaResultat2), E2 * -math.sin(thetaResultat1 + thetaResultat2)],
        [E1 * math.cos(thetaResultat1) + E2 * math.cos(thetaResultat1 + thetaResultat2), E2 * math.cos(thetaResultat1 + thetaResultat2)]
    ])
    dfdxinv = np.linalg.inv(dfdx)


    # calcul x - f1 et y - f2
    xf1 = bon_x - f1[0] 
    yf1 = bon_y - f1[1]
    xyf1 = np.array([xf1,yf1])
    print(f1)

    delta = dfdxinv @ xyf1

    thetaResultat1 = thetaResultat1 + delta[0]
    thetaResultat2 = thetaResultat2 + delta[1]
    f1 = [E1*math.cos(thetaResultat1)+E2*math.cos(thetaResultat1+thetaResultat2), E1*math.sin(thetaResultat1)+E2*math.sin(thetaResultat1+thetaResultat2)]

print("theta qui marchouille: ",thetaResultat1,thetaResultat2)
