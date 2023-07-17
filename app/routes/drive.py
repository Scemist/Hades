from flask import Blueprint
from controllers.IndexController import IndexController
from controllers.DriveController import DriveController

drive = Blueprint('drive', __name__)


@drive.route('/files')
def index():
    return DriveController.get_files()


@drive.route('/store')
def store():
    return DriveController.store()


@drive.route('/file')
def file():
    return DriveController.get_file_content()
