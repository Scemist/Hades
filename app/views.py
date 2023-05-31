from flask import Blueprint, render_template, url_for, request

blueprint = Blueprint('app', __name__)

@blueprint.route('/')
def home():
	return render_template('base.html', title='Hades - Landpage')

@blueprint.route('/new', methods=['POST'])
def about():
	return 'okay'