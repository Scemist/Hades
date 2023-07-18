const criptografia = () => { }

function iniciar() {
	const zaratustra = window.document.querySelector('#dark')
	const texto = window.document.querySelector('#texto')
	const inicio = window.document.querySelector('#inicio')

	zaratustra.addEventListener('click', () => {
		console.log('oi')
		texto.classList.toggle('aparente');
		inicio.classList.toggle('aparente')
	})

	return true
}

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

iniciar()
navbar()
criptografia()