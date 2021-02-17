const express = require('express')

const app = express()

app.use(require('cors')())
app.use('/Yuki', express.static('./'))

app.listen(8000)