# Hades
🗝 Hades faz o intermédio entre documentos de texto. Com um editor simples, criptografando e armazenando no Google Drive do usuário e lendo novamente com utilização de duas senhas.

## Tecnologias

- **Python** - as Base Language
- **Flask** - as Back-end Framework 
- **NGINX** - as WebServer
- **Gunicorn** - as WSGI
- **Google Drive Api** - as Storage
- **GPG AES256** - as Encryption Tool and Algorithm
- **TailwindCSS** - as Front-end Framework
- **Docker Compose** - as Application Infrastructure

## Privacidade

A API do Google Drive é utilizada envolvendo os seguintes escopos;

- drive.file
- drive.resource

Estes escopos são recomendados e não-sensíveis, uma vez que o Hades pode acessar apenas arquivos de sua criação ou que foram explicitamente dado acesso.

> [Google Drive Api Scopes](https://developers.google.com/drive/api/guides/api-specific-auth#scopes)
