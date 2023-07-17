import flask
import requests
from flask import render_template
from flask import Blueprint
import http.client

from env import *

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

from controllers.IndexController import IndexController
from controllers.AuthController import AuthController\

from pprint import pprint


class DriveController:
    def store():
        if 'credentials' not in flask.session:
            return ('You are not logged in Drive' + IndexController.index())

        credentials = google.oauth2.credentials.Credentials(
            **flask.session['credentials'])

        drive = googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, credentials=credentials)

        file_metadata = {
            'name': 'Project plan',
            'mimeType': 'application/vnd.google-apps.drive-sdk',
            'parents': ['appDataFolder'],
        }

        file = drive.files().create(body=file_metadata,
                                    fields='id').execute()

        return ('File created' + IndexController.index())

    def get_files():
        files = DriveController.request_files()
        return files

    def request_files():
        if 'credentials' not in flask.session:
            return ('You are not logged in Drive' + IndexController.index())

        credentials = google.oauth2.credentials.Credentials(
            **flask.session['credentials'])

        drive = googleapiclient.discovery.build(
            API_SERVICE_NAME,
            API_VERSION,
            credentials=credentials)

        files = drive.files().list(spaces="appDataFolder").execute()
        flask.session['credentials'] = AuthController.credentials_to_dict(
            credentials)

        return files
