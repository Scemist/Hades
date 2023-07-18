from flask import Blueprint
from flask import render_template
from flask import request
from controllers.IndexController import IndexController
from controllers.DriveController import DriveController

drive = Blueprint("drive", __name__)


@drive.route("/files")
def index():
    return DriveController.get_files()


@drive.route("/files/create", methods=["GET", "POST"])
def create_file():
    if request.method == "POST":
        return DriveController.store_file(
            request.values["title"], request.values["text_file"]
        )
    else:
        return render_template("create-file.html")


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
