const $icon = document.querySelector('.fas')
const $list = document.getElementById('nav_list')
const $button = document.getElementById('button_nav')
$icon.addEventListener('mouseover', ()=> {
    $list.classList.toggle('nav-list')
})
$button.addEventListener('mouseleave', ()=> {
    $list.classList.toggle('nav-list')
})
