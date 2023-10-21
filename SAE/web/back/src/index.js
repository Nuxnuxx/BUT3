import { app, config } from "./server.js"

app.listen(config.port, () => {
    console.log(`server on http://localhost:${config.port}`)
})
