import flask
import requests
from flask import render_template
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import session
import http.client
import io
from datetime import datetime

from drive_config import *

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.http import MediaIoBaseUpload

from controllers.IndexController import IndexController
from controllers.AuthController import AuthController
from controllers.EncryptController import EncryptController

from pprint import pprint


class DriveController:
    def store_file(filename, content):  # Redirect Home
        drive = AuthController.get_drive_service()

        content = EncryptController.encrypt(filename, content, session['key'])

        file_metadata = {
            "name": filename,
            "mimeType": "text/plain",
            "parents": [DriveController.get_app_folder()]
        }

        media = MediaIoBaseUpload(
            io.BytesIO(content), mimetype=file_metadata.get("mimeType")
        )

        file = (
            drive.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )

        return "File created" + IndexController.index()

    def store_app_folder():  # Redirect Home
        drive = AuthController.get_drive_service()

        file_metadata = {
            "name": "Hades",
            "mimeType": "application/vnd.google-apps.folder",
        }

        file = drive.files().create(body=file_metadata, fields="id").execute()

        return file.get('id')

    def get_app_folder():  # Id
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
            return DriveController.store_app_folder()

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

    def get_file(id):
        if not 'key' in flask.session:
            flash('You need to set and Encrypt Key First.')
            return redirect('/')

        drive = AuthController.get_drive_service()

        file_metadata = drive.files().get(fileId=id).execute()
        file = drive.files().get_media(fileId=id).execute()
        file = EncryptController.decrypt(file, flask.session['key'])

        return render_template("files-create.jinja", file=file, filename=file_metadata['name'], file_id=id)

    def get_files():
        DriveController.get_app_folder()

        drive = AuthController.get_drive_service()
        files = drive.files().list(
            q="trashed = false and mimeType != 'application/vnd.google-apps.folder'",
            fields='files(id, modifiedTime, createdTime, name, starred)').execute()

        def get_file_with_datetime(file):

            createdTime = datetime.strptime(
                file['createdTime'], "%Y-%m-%dT%H:%M:%S.%fZ")
            file['createdTime'] = createdTime.strftime('%d/%m/%Y')

            return file

        files['files'] = list(map(get_file_with_datetime, files['files']))

        return render_template("files.jinja", files=files["files"])

    def delete_file(id):
        drive = AuthController.get_drive_service()

        try:
            drive.files().delete(fileId=id).execute()
            flash('Arquivo deletado.')
        except Exception:
            flash('Ops! Erro ao deletar arquivo.')

        return DriveController.get_files()
