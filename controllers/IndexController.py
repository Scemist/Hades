from flask import render_template, session


class IndexController:
    def index(alert=None):
        key_setted = 'key' in session
        return render_template('drive.jinja', alert=alert, key_setted=key_setted)
