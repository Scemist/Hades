from flask import render_template

class IndexController:
    def index():
        return render_template('drive.html')