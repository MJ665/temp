const os = require ("os")

console.log(os.version())



const fs = require ("fs")
fs.open ("file.txt","w",function(err,file){
    if(err)throw err;
    console.log("saved")
})

fs.writeFile("file2.txt","hello content ",function(err){
    if (err)throw err;
    console.log('saved')
})

fs.appendFile("file3.txt","thsi si constnet appended",function(err){
    if(err)throw err;
    console.log("appending ")
})