import { Router } from "express"
import { body } from "express-validator"
import passwordOptions from "../utils/passwordOptions.js"
import { handleInputErrors } from "../modules/middleware.js"
import { protect } from "../modules/authentification.js"
import {
    changeUser,
    deleteUser,
    getUser,
    login,
    register,
} from "../handlers/user.js"

const userRouter = Router()

userRouter.post(
    "/register",
    body("mail").exists().isEmail(),
    body("firstname").exists().isString(),
    body("lastname").exists().isString(),
    body("gender").exists().isInt(),
    body("password").exists().isStrongPassword(passwordOptions),
    handleInputErrors,
    register,
)

userRouter.post(
    "/login",
    body("mail").exists().isEmail(),
    body("password").exists().isStrongPassword(passwordOptions),
    handleInputErrors,
    login,
)

userRouter.use(protect)

userRouter.get("/profil", getUser)
userRouter.put(
    "/profil",
    body("mail").optional().isEmail(),
    body("password").optional().isStrongPassword(passwordOptions),
    handleInputErrors,
    changeUser,
)

userRouter.delete("/profil", deleteUser)

export default userRouter
