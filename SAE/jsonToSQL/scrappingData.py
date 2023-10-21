import json

def recupDictJSON():
    with open('sample.json') as json_file:
        data = json.load(json_file)
    return data

def ajoutIngredient(idRecette, ingredient,ingredientAvecId,imageIngredientRecetteJSON, ingredientRecetteJSON,ingredientRecette):
    incrementIngredient= len(ingredientAvecId)
    parcoursIngredient =-1
    for imageIndredientJSON in imageIngredientRecetteJSON:
        parcoursIngredient+=1
        if imageIndredientJSON  not in ingredient:
            ingredient.append(imageIndredientJSON)
            ingredientAvecId.append({'idIngredient' :incrementIngredient,'nameIngredient':imageIndredientJSON[1],'pictureURL':imageIndredientJSON[0]})
            idIngredient= incrementIngredient
            incrementIngredient+=1
        else:
            idIngredient = ingredient.index(imageIndredientJSON)
        ingredientRecette.append({'idRecipe':idRecette,'idIngredient':idIngredient,'nameIngredient':ingredientRecetteJSON[parcoursIngredient]})

def ajoutSteps(idRecipe,steps):
    listSteps=[]
    incrementStep = 0
    for step in steps :
        listSteps.append({'idRecipe':idRecipe,'step':incrementStep,'name':step})
        incrementStep+=1
    return listSteps

def parcoursRecette(dictRecettes):
    recettes= []
    ingredient = []
    ingredientAvecId = []
    ingredientRecette=[]
    incrementIdRecette =0
    recetteStep =[]
    for recette in dictRecettes:
        recettes+=  [{'idRecipe':incrementIdRecette,'name':recette['Name'],'difficulty':recette['Difficulty'],'price':recette['Budget'],'quantity':recette['Recipe_Quantity']}]
        ajoutIngredient(incrementIdRecette, ingredient, ingredientAvecId, recette['Images_Ingredients'], recette["Ingredients"],ingredientRecette)
        recetteStep+=ajoutSteps(incrementIdRecette,recette['Steps'])
        incrementIdRecette+=1

    return ingredientAvecId,ingredientRecette,recetteStep,recettes
def convertJsonToSQL():
    dictRecette = recupDictJSON()
    sql= []
    ingredient, ingredientRecette,recetteStep,recipe = parcoursRecette(dictRecette)
    sql=dictTocript(ingredient,'ingredient',sql)
    sql = dictTocript(recipe,'recipe',sql)
    sql=dictTocript(ingredientRecette,'ingredientRecipe',sql)
    sql=dictTocript(recetteStep,'recipeStep',sql)

    with open('scriptSql.txt','a',encoding="utf-8") as file :
        for sqlLine in sql:
            file.write("\n"+sqlLine)



def dictTocript(listDico,nameTable,sql):
    for dico in listDico:
        colonne = ', '.join("`" + str(x).replace('/', '_') + "`" for x in dico.keys())
        valeur = ', '.join("'" + str(x).replace("'", "\\'").replace('/', '_') + "'" for x in dico.values())
        sql+= ["INSERT INTO %s ( %s ) VALUES ( %s ); " % (nameTable, colonne, valeur)]
    return sql + ["\n"]