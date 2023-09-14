## complexite

complexite => ordre de grandeur du cout de l'algo
              nombre operations elementaires pour obtenir le resultat a partir des donnees en entrees

operation valent 1 (afficher -> affectation -> return -> comparaison)
condition valent max + l'evaluation de la condition 
    (choisir le plus grand entre ce qu'il y a l'interieur du if ou du else)

boucle pour
    c'est une affection n fois (n connue)

boucle while
    meilleur cas -> x en premiere position
    pire cas -> x pas dans le tableau


## exo complexite
Fonction wits_first(n)
    pour i de 1 a n faire
        isastar vrai
        pour j de 1 à n faire
            si (i≠j) ET know(j,i)=faux
            isastar faux
        pour j de 1 à n faire
            si (i≠j) ET know(i,j)=vrai
            isastar faux
        si (isastar)
        retourner i
retourner 0

Fonction wits_first(n)
    i = 1, j = 2
    tant que (j <= n)
        si know(j,i) = faux
            i = j
        j = j + 1
    pour j de i+1 a n faire
         si know(i,j) = vrai
             retourner 0
retourner i
