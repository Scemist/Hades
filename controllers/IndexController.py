from flask import render_template


class IndexController:
    def index(alert = None):
        return render_template('drive.jinja', alert=alert)
