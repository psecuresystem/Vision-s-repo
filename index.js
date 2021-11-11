const express = require('express')
const app = express()
app.set('view-engine','ejs')
// app.use(express.urlencoded())
// app.use(express.json())

app.get('/',(req,res)=>{
    res.render('index.ejs')
})

app.listen(3000)