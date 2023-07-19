from flask import Blueprint
from flask import render_template
from flask import request
import flask
from controllers.IndexController import IndexController
from controllers.DriveController import DriveController
from controllers.AuthController import AuthController
from flask import flash
from flask import redirect

drive = Blueprint("drive", __name__)


@drive.before_request
def verify_auth():
    if not AuthController.check():
        flash('User not authenticated.')
        return redirect('/')


@drive.route("/files")
def index():
    return DriveController.get_files()


@drive.route("/files/create", methods=["GET", "POST"])
def create_file():
    if request.method == "POST":
        return DriveController.store_file(
            request.values["title"], request.values["text_file"], request.values["key"]
        )
    else:
        return render_template("create-file.jinja")


@drive.route("/store_file")
def store_file():
    return DriveController.store_file()


@drive.route("/folders/create/<folder_name>")
def store_folder(folder_name):
    return DriveController.store_folder(folder_name)


@drive.route("/folders/app-folder")
def get_app_folder():
    return DriveController.get_app_folder()


@drive.route("/file")
def file():
    return DriveController.get_file_content()
