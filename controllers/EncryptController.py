import gnupg
import base64


class EncryptController:
    def encrypt(filename, content, key):
        gpg = gnupg.GPG()

        result = gpg.encrypt(content, None, passphrase=key,
                             symmetric='AES256', armor=True)
        text = result.data
        # text = (base64.b64encode(result.data)).decode('ascii')

        return text

    def decrypt(key):
        return 'ho'
