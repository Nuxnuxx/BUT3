ALGORITHME rechercheSequentielle

VARIABLE
    ENTREE : 
        X : ENTIER
        TAB : Tableau d'entier
    SORTIE :
        ENTIER (representant l'index ou se situe l'objet rechercher si pas trouver -1)

DEBUT
    POUR i allant de 1 a taille(TAB)
        si tab[i] = X
            retourner i 
    retourner -1
FIN

## Cas favorable : 
    - L'objet rechercher est le premier de la liste
    - Le nombre de comparaison est donc de 1

## Cas defavorable : 
    - L'objet rechercher n'est pas dans la liste
    - Le nombre de comparaison est donc de n qui est la taille du tableau donne en parametre

probabilite de d : 1 / 4 car l'oppose de la probabilite qu'il soit dans le tableau
cout de traitement est de n operation car l'on doit parcourir tous le tableau comme l'objet rechercher n'est pas a l'interieur

la probabilite de d : 3 / 4 n car on multiple p par la probabilite qu'il soit dans chaque indice : 1 / n ce qui donne 3 / 4 n 
cout de traitement est donc de 1 car une seule comparasion sera necessaire pour trouver l'element comme il est en position 1

le cout moyen correspond au cout de toutes les position possible de l'element
rechercher donc si l'element est a la premier position 1, a la deuxieme il sera de 2 et ainsi de suite 
si l'element n'est pas dans la tableau il faudra faire n operations cela nous donne donc la suite 
1 + 2 + 3 + 4 .... + n qui a l'aide de la formure de la somme de n entier naturel donne : 


Le protocole serait le suivant : 
    - generer une liste represenant les n entier de 1 a 100 et rechercher l'entier 1 ce qui correspond au cas le plus favorable car cela correspond a 1 operation
    - generer une liste representant les n entier de 100 a 1 et rechercher l'entier 101 ce qui correspond au pire cas car l'entier rechercher n'est pas dans la liste donc n operations

