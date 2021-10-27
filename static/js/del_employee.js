const $id = document.getElementById('ID')
$id.addEventListener('keyup', ()=>{
    var id = $id.value
    if(id.length > 10){
        $id.value = ''
    }
    
})

const $back = document.getElementById('btnback')
$back.addEventListener('click', () =>{

    location.href="/login/admin"
})

const $del = document.getElementById('btndel')
$back.addEventListener('click', () =>{

    location.href="/admin/deleteEmployee/del"
})