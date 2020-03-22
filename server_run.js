const express = require('express')
const rateLimit = require('express-rate-limit')
const serveIndex = require('serve-index')
const path = require('path')
const app = express()
const port = 5000

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
})

app.use(limiter, express.static("log"), serveIndex("log", {'icons': true}));

app.listen(port, () => console.log(`Server running on port ${port}!`))
