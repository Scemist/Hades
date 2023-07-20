const Home = {
	load: () => {
		const zaratustra = document.querySelector('#dark')
		const texto = document.querySelector('#texto')
		const inicio = document.querySelector('#inicio')
	
		zaratustra.onclick = () => {
			texto.classList.toggle('aparente');
			inicio.classList.toggle('aparente')
		}
	
		this.navbar()
	},
	
	navbar: () => {
		const menu = document.querySelector('.menu')
		const pass = document.querySelector('#pass')
	
		menu.addEventListener('touchstart', () => {
			navigator.vibrate(50)
		})
	
		menu.addEventListener('touchend', () => {
			pass.classList.toggle('nav-ativada')
		})
	}
}

Home.load()