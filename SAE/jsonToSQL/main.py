# This is a sample Python script.

import json
import numpy as np
import csv

from sklearn_extra.cluster import KMedoids
import sklearn.preprocessing
from sklearn.cluster import KMeans

import scrappingData
import scrappingData as sd

import types
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def decoupeIngedient(ingredientListe,toutLesingredientPossible):
    L=[]
    for ingredient in ingredientListe:
        ingredient = ingredient.replace("d'","de ")
        ingredient = ingredient.split(' ')
        if len(ingredient)==1:
            quantite = ''
            unite = ''
            val= ingredient[0]

        elif "de" in ingredient:
            quantite = ingredient[0]
            unite = ingredient[1]
            val = ' '.join(ingredient[3:(len(ingredient))])
        else :
            quantite = ingredient[0]
            unite = ""
            val = ' '.join (ingredient[1:(len(ingredient))])
        if val not in toutLesingredientPossible:
            toutLesingredientPossible.append(val)
        L+=[[quantite, unite, val]]
    return L
def taFonction(recette1,recette2):

    sommeRecette = 0
    tailleRecette2 = len(recette2)
    sommeJ=0
    for i in range(0, len(recette1)):
        ingredient = recette1[i]
        j=0

        notIn = True
        while(notIn and j<tailleRecette2):

            if ingredient ==  recette2[j]:
                sommeRecette+=1
                notIn = False
            j+=1
    try:
        poids =sommeRecette/(len(recette1)+len(recette2))
    except:
        poids=0
    return poids




def calculPoids(tailleN,matrice,listeRecette):
    nbRecetteFait =0
    for i in range (0,tailleN):
        for j in range (0,tailleN ):
            recette1= listeRecette[i][1]
            recette2 = listeRecette[j][1]
            if i !=j :
                matrice[i][j]= taFonction(recette1,recette2)
            # if i == j :
            #     matrice[i][j] = 0
            nbRecetteFait+=1
            print(nbRecetteFait)
    return matrice

def recupIngredient(L):
    listeIngerdient= []
    for ingredient in L:
        if ingredient[1] not in listeIngerdient :
            listeIngerdient.append(ingredient[1])
    return listeIngerdient

def associeClusterRecette(L,listeRecette, nbCluster):
    monDict = dict()
    for  i in range (0, nbCluster):
        monDict[i]=[]
    for i in range (0,len(L)):
        monDict[L[i]].append(listeRecette[i])
    return monDict


if __name__ == '__main__':

    scrappingData.convertJsonToSQL()
#     i=0
#     with open('sample.json') as json_file:
#         data = json.load(json_file)
#         listeRecetteIngredient = []
#
#         for recipe in data:
#             recetteCoupe = [[recipe['Name']]]+ [recupIngredient(recipe["Images_Ingredients"])]+[convertDifficulty(recipe["Difficulty"])]+[convertTime]
#             listeRecetteIngredient += [recetteCoupe]
#
#
#     print(listeRecetteIngredient)
#     n = len(listeRecetteIngredient)-1
#     matrice = np.zeros((n,n))
#
#     calculPoids(n,matrice, listeRecetteIngredient)
#
#     with open('matrice.csv', 'w') as csv_file :
#         writer = csv.writer(csv_file)
#         for row in matrice:
#             writer.writerow(row)
#     print(matrice)
#
# scaler = sklearn.preprocessing.MinMaxScaler()
# matrice_similarite_normalisee = scaler.fit_transform(matrice)
#
#
# k = 20   # Choisis le nombre de clusters
# kmedoids = KMedoids(n_clusters=k, random_state=42)
# kmedoids.fit(matrice)
#
# # Obtenir les indices des médoides et les labels de cluster assignés
# medoids = kmedoids.medoid_indices_
# labels = kmedoids.labels_
#
# # Afficher les résultats
# print("Indices des médoides :", medoids)
# print("Labels de cluster :", labels)
#
#
# monDict = associeClusterRecette(labels,[listeRecetteIngredient[i][0] for i in range (0, len(listeRecetteIngredient))],k)
# for i in range (0,k):
#     clust = monDict[i]
#




