import flask
import requests
from flask import render_template
from flask import Blueprint
import http.client
import io

from env import *

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.http import MediaIoBaseUpload

from controllers.IndexController import IndexController
from controllers.AuthController import AuthController

from pprint import pprint


class DriveController:
    def store_file(file_name, content):  # Redirect Home
        AuthController.check()
        drive = AuthController.get_drive_service()

        file_metadata = {
            "name": file_name,
            "mimeType": "text/plain",
        }

        media = MediaIoBaseUpload(
            io.BytesIO(content.encode("utf-8")), mimetype=file_metadata.get("mimeType")
        )

        file = (
            drive.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )

        return "File created" + IndexController.index()

    def store_app_folder():  # Redirect Home
        AuthController.check()
        drive = AuthController.get_drive_service()

        file_metadata = {
            "name": "Hades",
            "mimeType": "application/vnd.google-apps.folder",
        }

        file = drive.files().create(body=file_metadata, fields="id").execute()

        return "File created" + IndexController.index()

    def get_app_folder():  # Id or False
        AuthController.check()
        drive = AuthController.get_drive_service()

        query = (
            "'root' in parents"
            " and mimeType = 'application/vnd.google-apps.folder'"
            " and name = 'Hades'"
            " and trashed = false"
        )

        folders = drive.files().list(q=query).execute()

        try:
            return folders["files"][0]["id"]
        except (KeyError, IndexError):
            return False

    # def store_file_contents():
    #     AuthController.check()
    #     drive = AuthController.get_drive_service()

    #     files = (
    #         drive.files()
    #         .get(fileId="1Y8B19QurZp4wgPUd6qjWPdAg4n3fMqFPyvss4FZP1LsYeDSbdAU")
    #         .execute()
    #     )
    #     flask.session["credentials"] = AuthController.credentials_to_dict(credentials)

    #     return files

    # def get_file_content():
    #     AuthController.check()
    #     drive = AuthController.get_drive_service()

    #     files = (
    #         drive.files()
    #         .get(
    #             alt="media",
    #             fileId="1Z2knnze5UHVGHejm6NbkKRUrghZf2b3np8XhJ2tBVj3Dx8ntAsU",
    #         )
    #         .execute()
    #     )

    #     flask.session["credentials"] = AuthController.credentials_to_dict(credentials)

    #     return files

    def get_files():
        AuthController.check()
        drive = AuthController.get_drive_service()
        files = drive.files().list(q="trashed = false").execute()

        return render_template("files.jinja", files=files["files"])
