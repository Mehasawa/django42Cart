
let likes = document.getElementsByClassName('like')
console.log(likes)

for (l of likes){
    l.onclick = f1
}


function f1(event){
    console.log(Math.random())
    console.log(event)
    console.log(event.target.id)
    let color
    if (event.target.src.includes('swhite')) {
        event.target.setAttribute('src','/static/img/sred.png')
        color='red'
    }
    else{
        event.target.setAttribute('src','/static/img/swhite.png')
        color='white'
    }
    let url = 'tolike/'
        $.ajax(url,{
            method:'GET',
            data:{k1:event.target.id, k2:color},
            success: function (response){
                console.log(response.message)
            },
            error: function (response){
                console.log('ошибка')
                console.log(response)
            }
        })

}