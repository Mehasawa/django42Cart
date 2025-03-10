

function f1(id,zakaz){
    console.log(id)
    elem = document.getElementById(id)
    console.log(elem.innerHTML)
    if (elem.innerHTML){
        elem.innerHTML = ''
    }
    else {
        elem.innerHTML = zakaz
    }
}