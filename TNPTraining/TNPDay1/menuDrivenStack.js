let a= [1,2,3,4,5]


function empty (){
    return a = []
}
function pushNum (n){
    return a.push(n) 
}

function popNum(n){
    if (length(a) == 0){
        return console.log("string is already empty")
    }
    return a.pop()
}

function main (){
    let operation = prompt ("enter the number ")
    if (operation == 0){
        empty()
    }if (operation == 1){
        let n = prompt ("enter the num")
        pushNum (n)
    }if (operation == 2){
        let n  = popNum()
        console.log("the poped number :" , n)
    }
}
main()