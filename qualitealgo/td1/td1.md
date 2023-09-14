Exercice 1

question 1 :

algo 1 
pour i = 1 a n faire            
    pour j = 1 a n faire        
        schtroumpfer           resultat : On2

algo 2
pour i = 1 a n faire           
    pour j = 1 a i faire       
        schtroumpfer           resultat : (n(n+1))/2 = On2

algo 3
pour i = 5 a n - 5 faire
    pour j = i - 5 a i + 5 faire    
        schtroumpfer                resultat : (n−9)×11=11n−9 = On

algo 4
pour i = 1 a n faire            
    pour j = 1 a i faire        
        pour k = 1 a j faire
            schtroumpfer            resultat : ∑i=1n 2i(i+1) On3


question 2 : plus généralement une boucle equivaut a un n

question 3 :
    Algo 1      Algo 2       Algo 3      Algo 4
10  100         45           10          120 
50  2500        1225         451         19600
100 10000       4950         1001        161700
200 40000       19900        2101        1313400

Exercice 2

Cout de l'Algo      1000             1 000 000           1 000 000 000
n                   1000             1 000 000           1 000 000 000
n log2 n            10000            20 000 000          30 000 000 000
n + 1 000 000 000   1 000 001 000    1 001 000 000       2 000 000 000
n2/1000 + 1000n     2 000 000        1 001 000 000 000   10puissance18 x 10puissance12

soit L une liste de n valeurs non ordonnée. Ces valeurs sont indicées de 1 à n dans L.
Rechercher la plus petite valeur entre les indice 1 et n et la positionner à l'indice 1, puis recommencer
cette opération entre les indice 2 et n, puis entre 3 et n, et ainsi de suite jusqu'à ce que la liste L soit
ordonnée.
• Ecrire en pseudocode l'algorithme triSelect(), en spécifiant les données et le résultat. L'indentation doit être irréprochable.

fonction triSelect(tableau L: entier)
    pour i de 1 a taille(L) - 1:
        indice_min = i
        pour j de i+1 a taille(L) - 1:
            si L[j] < L[indice_min]:
                indice_min = j;
            fin si
            si indice_min != i:
                échanger(L[i], L[indice_min])
            fin si
        fin pour
    retourner L
fin fonction

• Evaluer le coût d'une itération de votre algorithme
• En déduire le coût global et la complexité
