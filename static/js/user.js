alert("test user")
const _form = document.querySelector("#form")
const _button = document.getElementById("send")

function renderData(user, pass, image, video){
    const user = document.getElementById('previewName')
    const password = document.getElementById('previewPassword')
    const image = document.getElementById('previewImage')
    const video = document.getElementById('previewVideo')
    user.textContent(user)
    password.textContent(password)
}
_button.addEventListener("click", (event) => {
    event.preventDefault()
    const form = new FormData(_form)
    const user = form.get('username')
    const password = form.get('password')
    const image = form.get('image')
    const video = form.get('video')
    renderData(user, password, image, video)
}
)