import bcrypt from "bcrypt"
import jwt from "jsonwebtoken"

export const comparePasswords = (password, hash) => {
    return bcrypt.compare(password, hash)
}

export const hashPassword = (password) => {
    return bcrypt.hash(password, 5)
}

export const createJWT = (mail) => {
    const token = jwt.sign({ mail: mail }, process.env.JWT_SECRET, {
        expiresIn: "30d",
    })

    return token
}

export const protect = (req, res, next) => {
    const bearer = req.headers.authorization

    if (!bearer) {
        res.status(401)
        res.json({ message: "not authorized" })
        return
    }

    const [, token] = bearer.split(" ")

    if (!token) {
        res.status(401)
        res.json({ message: "not valid token" })
        return
    }

    try {
        const user = jwt.verify(token, process.env.JWT_SECRET)
        req.user = user
        next()
    } catch (e) {
        res.status(401)
        res.json({ message: "not valid token" })
        return
    }
}
