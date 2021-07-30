# Hades

Hades faz o intermédio entre documentos, criptografando e armazenando no Google Drive e lendo novamento com utilização das chaves.

## Descrição do Código

> * Na **index.php**, há uma lista de arquivos da pasta **/documentos/**.
> * No rodapé, há um campo para colocar o nome do arquivo e um botão para criar.
> * É iniciada uma função no arquivo **documento.php** que manda uma solicitação para o arquivo **arquivo.php**.
> * Uma função do PHP retorna uma lista JSON para o JavaScript, sem atualizar a página, em Ajax.
> * O JavaScript atualiza a lista da **index** com a nova lista PHP
