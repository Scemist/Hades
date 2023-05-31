// Listeners dos Métodos da classe Documento

criarListener()
abrirListener()
salvarListener()

function criarListener() { // Cria o listener que chama a função para criar um novo arquivo por Ajax
	const criar = document.querySelector('#criar')

	criar.onclick = () => {
		const nome = document.querySelector('#nome').value

		const doc = new documento(nome)
		doc.criarArquivo()
	}
}

function abrirListener() { // Cria o listener que chama a função para abrir o arquivo no editor

	var arquivos = document.getElementsByTagName('button')

	for (var controle = 0; controle < arquivos.length; controle++) {

		arquivos[controle].addEventListener('click', function (controle) {

			var instancia = new documento()
			globalThis.arquivoAtual = instancia.abrirArquivo(controle)
		}.bind(null, controle))
	}
}

function salvarListener() { // Cria o listener que chama a função para salvar o arquivo

	const salvar = window.document.querySelector('#salvar')

	salvar.addEventListener('click', function () {

		var instancia = new documento()
		instancia.salvarArquivo(arquivoAtual)
	})
}

class documento {

	constructor(nome, titulo, corpo) {

		this.nome = nome
		this.titulo = titulo
		this.corpo = corpo
	}

	criarArquivo() { // Função que cria o novo arquivo e retorna a lista atualizada de arquivos

		const xhr = new XMLHttpRequest()
		const listaDocumentos = window.document.querySelector('#listaDocumentos')

		xhr.open("POST", "../php/arquivo.php")
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
		xhr.send('titulo=' + this.nome + '&tipo=criar')
		xhr.onreadystatechange = function () {

			if (xhr.readyState === 4 && xhr.status === 200) {

				var lista = JSON.parse(xhr.responseText)
				var matriz = []

				for (var i in lista) { // Adiciona o Objeto JSON à uma array
					matriz.push(lista[i])
				}

				listaDocumentos.innerHTML = ''

				matriz.forEach(nomeArquivo => { // Constrói os arquivos na array na tela

					var botao = document.createElement("button")
					botao.className = 'lista'
					botao.innerText = nomeArquivo
					listaDocumentos.appendChild(botao)
				})

				abrirListener()
			} else {

				console.log('. . .')
			}
		}

		return true
	}

	salvarArquivo(arquivoAtual) { // Função que salva o arquivo a partir do editor

		const corpo = window.document.querySelector('#p-corpo').innerText
		const xhr = new XMLHttpRequest()

		xhr.open('POST', '/new')
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
		xhr.send('titulo=' + arquivoAtual + '&tipo=salvar&corpo=' + corpo)
		xhr.onreadystatechange = function () {

			if (xhr.readyState === 4 && xhr.status === 200) {

				if (xhr.responseText == true) {

					console.log('A vida é uma caixinha de acontecimentos violentos.')
					window.alert('À Bússula.')
				} else {

					window.alert('Hm, há algo errado, Scemist')
				}
			}
		}

		return true
	}

	abrirArquivo(index) { // Abre o arquivo no editor

		this.nome = document.getElementsByTagName('button')[index].innerText
		const texto = window.document.querySelector('#texto')
		const inicio = window.document.querySelector('#inicio')
		const pCorpo = window.document.querySelector('#p-corpo')
		var xhr = new XMLHttpRequest

		pCorpo.innerText = ''
		texto.classList.toggle('aparente');
		inicio.classList.toggle('aparente')

		xhr.open('POST', '../php/arquivo.php')
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
		xhr.send('titulo=' + this.nome + '&tipo=pegarConteudo')
		xhr.onreadystatechange = function () {

			if (xhr.readyState == 4 && xhr.status == 200) {

				var conteudo = xhr.responseText
				pCorpo.innerText = conteudo
			}
		}

		return this.nome
	}

	deletarArquivo() { // Deleta o arquivo

		return true
	}
}