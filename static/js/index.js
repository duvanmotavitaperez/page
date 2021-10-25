const $form = document.getElementById('form')
const $button =document.getElementById('send')

$button.addEventListener('click', (event)=>{   
    event.preventDefault()
    const form = new FormData($form)
    fetch(`${window.origin}/send`, {
        method: 'POST',
        body: form
    })
    .then(function(response){
        window.location.href = `${window.origin}/app`
    })
})