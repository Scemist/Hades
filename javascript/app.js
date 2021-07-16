const criptografia = () => {}

const navbar = () => {

    const menu = document.querySelector('.menu')
    const pass = document.querySelector('#pass')

    menu.addEventListener('touchstart', () => {

        navigator.vibrate(50)
    })

    menu.addEventListener('touchend', () => {

        pass.classList.toggle('nav-ativada')
    }) 
}

criptografia()
navbar()

