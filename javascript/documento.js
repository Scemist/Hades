function criarListener() { // Create the listener that calls the class 'document' to create a new file by Ajax
    
    const criar = window.document.querySelector('#criar')
    criar.addEventListener('click', () => {
        
        var nome = window.document.querySelector('#nome').value
        
        var doc = new documento(nome)
        doc.criarArquivo()
    })
}

criarListener()

// ------------------------------------------------------------------------------------------

class documento {

    constructor(nome, titulo, corpo) {

        this.nome = nome
        this.titulo = titulo
        this.corpo = corpo
    }

    criarArquivo() { // Function that creates the new file and return the updated list of files
    
        const xhr = new XMLHttpRequest()    

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
                
                matriz.forEach(element => {
                    
                    console.log(element)
                });

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

    deletarArquivo() {

        return true
    }
}