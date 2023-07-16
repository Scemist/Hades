from flask import Blueprint
from controllers.IndexController import IndexController
from controllers.DriveController import DriveController

drive = Blueprint('drive', __name__)

@drive.route('/files')
def index():
	return DriveController.get_files()