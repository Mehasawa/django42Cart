
let but1 = document.getElementById('but1')
let form1 = document.getElementById('form1')

let visible = false
function f1(){
    console.log(Math.random())
    if (!visible){
        form1.hidden = false
        visible = true
    }
    else{
        form1.hidden = true
        visible = false
    }
}

but1.onclick = f1