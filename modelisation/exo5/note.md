# Homographie : c'est une transformation entre deux plan

## Notation 
- Photo 1 -> I1
- Photo 2 -> I2

- Un point de I1 -> x1
- Un point de I2 -> x2


- x1 -> represente deux coordonnes du point dans le repere de I1

- x2 -> ""              ""                  dans le repere de I2


Il existe une matrice de dimesion 2x2 qui relie des coordonnes x1 et x2. c'est une Homographie.
Sous forme matricielle, 

on peut ecrire x1 = H.x2
ou encore (wu1 wv2 w) =  H.x2
                       
                      


1ere etape : o estime la matrice H Pour ca on va developper le calcul 


(wu1 wv2 w) = (h11 h12 h13) (u2 v2 1)
                        (h21 h22 h23)
                        (h31 h32 h33)

wu1 = h11 u2 + h12 v2 + h13
wv1 = h21 u2 + h22 v2 + h23
w = h31 u2 + h32 v2 + 1
