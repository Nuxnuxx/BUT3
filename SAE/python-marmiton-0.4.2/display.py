from marmiton import Marmiton, RecipeNotFound
import json


total = 0
listJson = []

for j in range(1, 84):
    print("page : " + str(j))
    # Search :
    query_options = {
    "aqt": "",  # Query keywords - separated by a white space
    #"dt": "",       # Plate type : "entree", "platprincipal", "accompagnement", "amusegueule", "sauce" (optional)
    #"exp": 2,                    # Plate price : 1 -> Cheap, 2 -> Medium, 3 -> Kind of expensive (optional)
    #"dif": 2,                    # Recipe difficulty : 1 -> Very easy, 2 -> Easy, 3 -> Medium, 4 -> Advanced (optional)
    #"veg": 0,                    # Vegetarien only : 0 -> False, 1 -> True (optional)
    "page": j,                  # Page number (optional)   
    }
    query_result = Marmiton.search(query_options)

    recipe = query_result
    total += len(recipe)
    # Get :
    for i in range(len(recipe)):
        
        #print nombre de recettes
        main_recipe_url = recipe[i]['url']

        try:
            detailed_recipe = Marmiton.get(main_recipe_url)  # Get the details of the first returned recipe (most relevant in our case)
        except RecipeNotFound as e:
            print(f"No recipe found for '{query_options['aqt']}'")
            import sys
            sys.exit(0)

        # Display result :
        # Create a dictionary with the data
        recipe_data = {
            "Name": detailed_recipe['name'],
            "Rating": detailed_recipe['rate'],
            "Cook_Time": detailed_recipe['cook_time'] if detailed_recipe['cook_time'] else 'N/A',
            "Preparation_Time": detailed_recipe['prep_time'],
            "Total_Time": detailed_recipe['total_time'],
            "Difficulty": detailed_recipe['difficulty'],
            "Budget": detailed_recipe['budget'],
            "Recipe_Quantity": detailed_recipe['recipe_quantity'],
            "Ingredients": detailed_recipe['ingredients'],
            "Images": detailed_recipe['images'],
            "Images_Ingredients": detailed_recipe['images_ingredients'],
            "Steps": detailed_recipe['steps'],
        }

        if detailed_recipe['author_tip']:
            recipe_data["Author_Tip"] = detailed_recipe['author_tip']

        listJson.append(recipe_data)

#mettre l'encodage en utf-8
recipe_json = json.dumps(listJson, indent=4, ensure_ascii=False)

with open('recipe_json', 'w', encoding='utf-8') as f:
    f.write(recipe_json)


print("")
print("")
print("")
print(total)
print("")
print("")
print("")