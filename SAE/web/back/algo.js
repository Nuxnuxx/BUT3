const createRandomArray = (size) => {
    const result = []
    // Boucle de creation de tableu de valeur aleatoire
    for (let i = 0; i < size; i++) {
        // Taille aleatoire entre 1 et 10
        const finalArraylength = Math.ceil(Math.random() * 10)
        const finalArray = new Array(finalArraylength)

        // Ajout de nombre aleatoire entre 1 et 15
        for (let i = 0; i < finalArraylength; i++) {
            finalArray[i] = Math.ceil(Math.random() * 15)
        }
        result.push(finalArray)
    }
    return result
}

const navigationCompute = (navigationArray) => {
    let result = []
    navigationArray.map((nav) => {
        for (let i = 0; i < nav.length - 1; i++) {
            // si la recette cliquee est deux fois la meme
            // alors on passe exemple 3 puis 3
            if (nav[i] === nav[i + 1]) {
                continue
            }

            const recipe = result.find((item) => item.recipe == nav[i])

            // si la recette existe deja alors on verifie
            // si la recette cible existe
            if (recipe) {
                const recipeTarget = recipe.recipeTarget.find(
                    (element) => element.id == nav[i + 1],
                )

                // si elle existe on incremente juste son compteur sinon on
                // creer la recette cible
                if (recipeTarget) {
                    recipeTarget.count += 1
                } else {
                    const recipeTarget = {
                        id: nav[i + 1],
                        count: 1,
                    }
                    recipe.recipeTarget.push(recipeTarget)
                }
            } else {
                // si la recette n'existe pas alors on la creer et
                // on push sa premiere cible
                const temp = {
                    recipe: nav[i],
                    recipeTarget: [],
                }
                const recipeTarget = {
                    id: nav[i + 1],
                    count: 1,
                }

                temp.recipeTarget.push(recipeTarget)
                result.push(temp)
            }
        }
    })

    return result
}

const beforeArray = createRandomArray(3)
const resultArray = navigationCompute(beforeArray)

resultArray.map((element) => {
    console.log(element)
})
