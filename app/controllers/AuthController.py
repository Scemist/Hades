import flask
import requests
from flask import render_template
from flask import Blueprint

from env import *

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

class AuthController:
	def test_api_request():
		if 'credentials' not in flask.session:
			return flask.redirect('authorize')

		credentials = google.oauth2.credentials.Credentials(
			**flask.session['credentials'])

		drive = googleapiclient.discovery.build(
			API_SERVICE_NAME, API_VERSION, credentials=credentials)

		files = drive.files().list().execute()
		flask.session['credentials'] = AuthController.credentials_to_dict(credentials)

		return flask.jsonify(**files)

	def credentials_to_dict(credentials):
		return {'token': credentials.token,
				'refresh_token': credentials.refresh_token,
				'token_uri': credentials.token_uri,
				'client_id': credentials.client_id,
				'client_secret': credentials.client_secret,
				'scopes': credentials.scopes}
