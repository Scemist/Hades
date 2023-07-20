import gnupg
import base64
from flask import session


class EncryptController:
    def encrypt(filename, content, key):
        EncryptController.set_password_cookie(key)

        gpg = gnupg.GPG()

        result = gpg.encrypt(content, None, passphrase=key,
                             symmetric='AES256', armor=True)
        text = result.data
        # text = (base64.b64encode(result.data)).decode('ascii')

        return text

    def decrypt(file, key):
        gpg = gnupg.GPG()

        result = gpg.decrypt(file, passphrase=key)
        return result.data

    def set_password_cookie(key):
        session['key'] = key
