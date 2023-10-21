import config from "./config/index.js"
import express from "express"
import morgan from "morgan"
import cors from "cors"
import userRouter from "./router/user.js"
import recipeRouter from "./router/recipe.js"

const app = express()

app.use(morgan("dev"))
app.use(express.json())

app.use(express.urlencoded({ extended: true }))
app.use(
    cors({
        credentials: true,
        origin: config.origin,
    }),
)

app.use("/user", userRouter)
app.use("/recipe", recipeRouter)

// Contains all the navigation of the user
const navigation = []
app.set("navigation", navigation)

app.use((err, req, res, next) => {
    if (err.type === "auth") {
        res.status(401).json({ errors: "unauthorized" })
    } else if (err.type === "input") {
        res.status(409).json({ errors: "invalid input" })
    } else {
        res.status(500).json({ errors: "server error" })
    }
})

export { app, config }
