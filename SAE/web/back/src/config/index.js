import dotenv from "dotenv"
dotenv.config()
import prod from "./prod.js"
import local from "./local.js"
import testing from "./testing.js"
import merge from "lodash.merge"

process.env.NODE_ENV = process.env.NODE_ENV || "development"

const stage = process.env.STAGE || "local"
let envConfig = {}

if (stage === "production") {
    envConfig = prod
} else if (stage === "testing") {
    envConfig = testing
} else {
    envConfig = local
}

export default merge(
    {
        stage,
        env: process.env.NODE_ENV,
        origin: "http://localhost:5173",
        port: 3001,
        secrets: {
            host: process.env.DATABASE_PROD_HOST,
            user: process.env.DATABASE_PROD_USER,
            database: process.env.DATABASE_PROD_DATABASE,
            password: process.env.DATABASE_PROD_PASSWORD,
        },
    },
    envConfig,
)
