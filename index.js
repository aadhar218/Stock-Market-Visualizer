'use strict';
const express = require('express');
const app = express();
app.listen(8888,() => console.log("listening"));
app.use(express.static('public'));
app.use(express.json({limit:'1mb'}));