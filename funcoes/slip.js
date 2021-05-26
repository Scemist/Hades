const inicio = () => {

    window.console.log('Chão escorregadio.')
}

const requisicao = () => {

    const requisicao = window.document.querySelector('#requisicao')
    const conteudo = window.document.querySelector('#conteudo')
    const xhr = new XMLHttpRequest()

    requisicao.addEventListener('click', () => {

        xhr.open("GET", "funcoes/knot.php")
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

inicio()
requisicao()