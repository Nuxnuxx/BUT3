import prisma from "../db.js"
import {
    comparePasswords,
    createJWT,
    hashPassword,
} from "../modules/authentification.js"

export const register = async (req, res, next) => {
    try {
        const user = await prisma.user.create({
            data: {
                mail: req.body.mail,
                firstname: req.body.firstname,
                lastname: req.body.lastname,
                gender: req.body.gender,
                password: await hashPassword(req.body.password),
            },
            select: {
                mail: true,
            },
        })

        if (!user) {
            return res.status(500).json({ message: "User not created" })
        }

        const token = createJWT(user.mail)
        res.json({ token })
    } catch (error) {
        console.error(error)
        error.type = "input"
        next(error)
    }
}

export const login = async (req, res, next) => {
    try {
        const user = await prisma.user.findUnique({
            where: {
                mail: req.body.mail,
            },
        })

        if (!user) {
            return res.status(404).json({ message: "User not found" })
        }

        const isValid = await comparePasswords(req.body.password, user.password)

        if (!isValid) {
            return res.status(401).json({ message: "Invalid password" })
        }

        const token = createJWT(user.id)
        res.json({ token })
    } catch (error) {
        console.error(error)
        error.type = "input"
        next(error)
    }
}

export const getUser = async (req, res, next) => {
    try {
        const user = await prisma.user.findUnique({
            where: {
                mail: req.user.mail,
            },
        })

        if (!user) {
            return res.status(404).json({ message: "User not found" })
        }

        res.json({ user })
    } catch (error) {
        console.error(error)
        error.type = "input"
        next(error)
    }
}

export const changeUser = async (req, res, next) => {
    try {
        const { mail, password } = req.body
        const updateData = {}

        if (mail) {
            updateData.mail = mail
        }

        if (password) {
            updateData.password = password
        }

        const user = await prisma.user.update({
            where: {
                mail: req.user.mail,
            },
            data: updateData,
            select: {
                mail: true,
            },
        })

        const token = createJWT(user.mail)
        res.json({ token })
    } catch (error) {
        console.error(error)
        error.type = "input"
        next(error)
    }
}

export const deleteUser = async (req, res, next) => {
    try {
        const user = await prisma.user.delete({
            where: {
                mail: req.user.mail,
            },
        })

        res.json({ user })
    } catch (error) {
        error.type = "input"
        next(error)
    }
}
