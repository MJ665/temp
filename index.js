var http = require ("http")
var uc = require ("upper-ccase")

http.createServerer(function(req,res){
    res.writeHead(200,{"Content-Head":"text/html"})
    res.write(uc.upperCase("hello world"))
    res.end()
}).listen(8080)