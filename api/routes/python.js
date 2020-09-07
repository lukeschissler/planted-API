var express = require("express");
var router = express.Router();


router.get("/", (req, res, next) => {
    const {spawn} = require('child_process');
    const python = spawn('python', ['script.py'])

    python.stdout.on('data', (data) => {
        console.log(data.toString());
        res.write(data);
        res.end('end')
    });

});

module.exports = router;