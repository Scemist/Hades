import gnupg
import base64
from flask import session
from flask import flash


class EncryptController:
    def encrypt(filename, content, key):
        EncryptController.set_password_cookie(key)

        gpg = gnupg.GPG()
        gpg.encoding = "utf-8"

        result = gpg.encrypt(
            content, None, passphrase=key, symmetric="AES256", armor=True
        )
        text = result.data

        return text

    def decrypt(file, key):
        gpg = gnupg.GPG()
        gpg.encoding = "utf-8"

        result = gpg.decrypt(file, passphrase=key)

        if not result.ok:
            flash("Decrypt failed. Is the key correct for this file?", "danger")

        return result.data.decode("utf-8")

    def set_password_cookie(key):
        session["key"] = key
