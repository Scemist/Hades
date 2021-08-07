// Listeners dos Métodos da classe Documento

criarListener()
abrirListener()

function criarListener() { // Create the listener that calls the class 'document' to create a new file by Ajax

    const criar = window.document.querySelector('#criar')
    criar.addEventListener('click', () => {
        
        var nome = window.document.querySelector('#nome').value
        
        var doc = new documento(nome)
        doc.criarArquivo()
    })
}

function abrirListener() {

    var arquivos = document.getElementsByTagName('button');

    for (var controle = 0; controle < arquivos.length; controle++) {

        arquivos[controle].addEventListener('click', function(controle) {
            
            var instancia = new documento()
            instancia.abrirArquivo(controle)
        }.bind(null, controle));
    }
}

// Classe Documento

class documento {

    constructor(nome, titulo, corpo) {

        this.nome = nome
        this.titulo = titulo
        this.corpo = corpo
    }

    criarArquivo() { // Function that creates the new file and return the updated list of files
    
        const xhr = new XMLHttpRequest()    
        const listaDocumentos = window.document.querySelector('#listaDocumentos')

        xhr.open("POST", "../php/arquivo.php")
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
        xhr.send('titulo=' + this.nome + '&tipo=criar')

        xhr.onreadystatechange = function() {

            if (xhr.readyState === 4 && xhr.status === 200) {

                var lista = JSON.parse(xhr.responseText) // 'lista' is the json array 
                var matriz = []

                for (var i in lista) {

                    matriz.push(lista[i])
                }

                listaDocumentos.innerHTML = ''

                matriz.forEach(nomeArquivo => {
                
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

    salvarArquivo() {

        const salvar = window.document.querySelector('#salvar')
    
        salvar.addEventListener('click', () => {
    
            const corpo = window.document.querySelector('#p-corpo').innerText
            window.document.querySelector('#corpo').value = corpo
        })

        return true
    }

    abrirArquivo(index) {

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

    deletarArquivo() {

        return true
    }
}