from flask import Blueprint, render_template, url_for

blueprint = Blueprint('app', __name__)

@blueprint.route('/')
def home():
	return render_template('base.html', title='Hades - Landpage')

@blueprint.route('/about')
def about():
	return render_template('base.html')