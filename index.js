import http from "http"


import { upperCase as uc } from "upper-case";

http.createServer(function(req, res) {
    res.writeHead(200, {"Content-Type": "text/html"});
    res.write(uc("hello world"));
    res.end();
}).listen(8080);
