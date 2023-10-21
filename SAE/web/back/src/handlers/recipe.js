import prisma from "../db.js"

export const getRecipe = async (req, res) => {
    try {
        const recipe = await prisma.order.findUnique({
            where: {
                idRecipe: req.params.id,
            },
        })

        if (!recipe) {
            return res.status(404).json({ message: "Order not found" })
        }

        res.json({ recipe })
    } catch (error) {
        console.error(error)
        error.type = "input"
        next(error)
    }
}

export const getRecipes = async (req, res) => {
    // find recipe with pagination
}

export const getRecipesByKeyword = async (req, res) => {
    // find recipe with pagination and filter by keyword
}
