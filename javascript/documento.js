// Listeners dos Métodos da classe Documento

criarListener()
abrirListener()

function criarListener() { // Cria o listener que chama a função para criar um novo arquivo por Ajax
    

    const criar = window.document.querySelector('#criar')
    criar.addEventListener('click', () => {
        
        var nome = window.document.querySelector('#nome').value
        
        var doc = new documento(nome)
        doc.criarArquivo()
    })
}

function abrirListener() { // Cria o listener que chama a função para abrir o arquivo no editor

    var arquivos = document.getElementsByTagName('button')

    for (var controle = 0; controle < arquivos.length; controle++) {

        arquivos[controle].addEventListener('click', function(controle) {
            
            var instancia = new documento()
            instancia.abrirArquivo(controle)
        }.bind(null, controle))
    }
}

// Classe Documento

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
        xhr.onreadystatechange = function() {

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

    salvarArquivo() { // Função que salva o arquivo a partir do editor

        const salvar = window.document.querySelector('#salvar')
    
        salvar.addEventListener('click', () => {
    
            const corpo = window.document.querySelector('#p-corpo').innerText
            window.document.querySelector('#corpo').value = corpo
        })

        return true
    }

    abrirArquivo(index) { // Abre o arquivo no editor

        this.nome = document.getElementsByTagName('button')[index].innerText
        const texto = window.document.querySelector('#texto')
        const inicio = window.document.querySelector('#inicio')
        const pCorpo = window.document.querySelector('#p-corpo')
        var xhr = new XMLHttpRequest

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
    }

    deletarArquivo() { // Deleta o arquivo

        return true
    }
}