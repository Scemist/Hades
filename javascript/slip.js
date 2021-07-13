const inicio = () => {

    window.console.log('Chão escorregadio.')
}

const requisicao = () => {

    const requisicao = window.document.querySelector('#requisicao')
    const conteudo = window.document.querySelector('#conteudo')
    const xhr = new XMLHttpRequest()

    requisicao.addEventListener('click', () => {

        xhr.open("GET", "../php/knot.php")
        xhr.send()

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {

                conteudo.innerHTML = xhr.responseText
            } else {

                conteudo.innerHTML = ". . ."
            }
        }
    })
}

const arquivo = () => {

    const salvar = window.document.querySelector('#salvar');

    salvar.addEventListener('click', () => {

        const corpo = window.document.querySelector('#p-corpo').innerText
        window.document.querySelector('#corpo').value = corpo
    })
}

inicio()
requisicao()
arquivo()