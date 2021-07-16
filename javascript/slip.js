const iniciar = () => {

    const zaratustra = window.document.querySelector('#dark')
    const texto = window.document.querySelector('#texto')
    const inicio = window.document.querySelector('#inicio')

    zaratustra.addEventListener('click', () => {

        console.log('oi')
        texto.classList.toggle('aparente');
        inicio.classList.toggle('aparente')
    })
}

const criarArquivo = () => {

    const criar = window.document.querySelector('#criar')
    const xhr = new XMLHttpRequest()

    criar.addEventListener('click', () => {

        const titulo = window.document.querySelector('#titulo').value
        xhr.open("POST", "../php/arquivo.php")
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send('titulo=' + titulo + '&tipo=criar')

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {

                console.log(xhr.responseText)
            } else {

                console.log('. . .')
            }
        }
    })
}

const pegarTexto = () => {

    const salvar = window.document.querySelector('#salvar');

    salvar.addEventListener('click', () => {

        const corpo = window.document.querySelector('#p-corpo').innerText
        window.document.querySelector('#corpo').value = corpo
    })
}

iniciar()
criarArquivo()
pegarTexto()