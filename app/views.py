from flask import Blueprint, render_template, url_for

blueprint = Blueprint('app', __name__)

@blueprint.route('/about')
def about():
	return render_template('base.html')