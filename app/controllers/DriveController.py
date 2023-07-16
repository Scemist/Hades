import flask
import requests
from flask import render_template
from flask import Blueprint

from env import *

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

from controllers.IndexController import IndexController
from controllers.AuthController import AuthController

class DriveController:
	def get_files():
		if 'credentials' not in flask.session:
			return ('You are not logged in Drive' + IndexController.index())

		credentials = google.oauth2.credentials.Credentials(
			**flask.session['credentials'])

		drive = googleapiclient.discovery.build(
			API_SERVICE_NAME, API_VERSION, credentials=credentials)

		files = drive.files().list().execute()
		flask.session['credentials'] = AuthController.credentials_to_dict(
			credentials)

		return files