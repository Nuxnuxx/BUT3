import { Router } from "express"
import { param } from "express-validator"
import { handleInputErrors } from "../modules/middleware.js"
import {
    getRecipe,
    getRecipes,
    getRecipesByKeyword,
} from "../handlers/recipe.js"

const recipeRouter = Router()

recipeRouter.get(
    "/recipe/:id",
    param("id").exists().isInt(),
    handleInputErrors,
    getRecipe,
)

recipeRouter.get("/recipes", getRecipes)

recipeRouter.get("recipesSearch/:keyword", getRecipesByKeyword)

recipeRouter.get("recipesSearch/:filter/:value", getRecipesByKeyword)

export default recipeRouter
