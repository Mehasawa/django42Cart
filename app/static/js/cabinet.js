

function f1(id,zakaz){
    console.log(zakaz)
    elem = document.getElementById(id)
    console.log(elem.innerText)
    if (elem.innerText){
        elem.innerHTML=''
    }
    else{
         elem.innerHTML = zakaz
    }
}