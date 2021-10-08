const $form = document.querySelector("#form")
const $button = document.getElementById("button2")
function renderData(_user, _pass, _image, _video){
    const user = document.getElementById('previewName')
    const password = document.getElementById('previewPassword')
    const image = document.getElementById('previewImage')
    const video = document.getElementById('previewVideo')
    const urlImage = URL.createObjectURL(_image)
    user.textContent = _user
    password.textContent = _pass
    image.setAttribute('src', urlImage)
}

$form.addEventListener('submit', (event) => {
    event.preventDefault()
    fetch('/uploadFiles', {
        method: 'POST', 
        body: FormData($form),
    }) 
    .then(event => {
        document.write('Finally')
    })
})