// import http from "http"


// import { upperCase as uc } from "upper-case";


const http = require("http")
const uc = require("upper-case")


http.createServer(function(req, res) {
    res.writeHead(200, {"Content-Type": "text/html"});
    res.write(uc.upperCase("hello world"));
    res.end();
}).listen(8080);
