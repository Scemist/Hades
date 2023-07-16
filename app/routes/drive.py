from flask import Blueprint
from controllers.IndexController import IndexController
from controllers.AuthController import AuthController

drive = Blueprint('drive', __name__)

@drive.route('/files')
def index():
	return 'AHH'