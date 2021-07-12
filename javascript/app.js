const criptografia = () => {}

const navbar = () => {

    const menu = document.querySelector('.menu')
    const nav = document.querySelector('nav')

    menu.addEventListener('touchstart', () => {

        navigator.vibrate(50)
    })

    menu.addEventListener('touchend', () => {

        nav.classList.toggle('nav-ativada')
    }) 
}

criptografia()
navbar()

