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
        flash("User not authenticated.")
        return redirect("/")


@drive.route("/files")
def index():
    return DriveController.get_files()


@drive.route("/files/<id>")
def get_file(id):
    return DriveController.get_file(id)


@drive.route("/files/delete/<id>", methods=["GET", "DELETE"])
def delete_file(id):
    return DriveController.delete_file(id)


@drive.route("/files/create", methods=["GET", "POST"])
def create_file():
    if request.method == "POST":
        return DriveController.store_file(
            request.values["title"], request.values["text_file"]
        )
    else:
        return render_template("files-create.jinja", create=True)


# @drive.route("/store_file")
# def store_file():
#     return DriveController.store_file()


@drive.route("/folders/create/<folder_name>")
def store_folder(folder_name):
    return DriveController.store_folder(folder_name)


@drive.route("/folders/app-folder")
def get_app_folder():
    return DriveController.get_app_folder()


@drive.route("/file")
def file():
    return DriveController.get_file_content()

@drive.route("/info")
def user_info():
    return AuthController.get_user_info()
