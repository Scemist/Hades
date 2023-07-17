import flask
import requests
from flask import render_template
from flask import Blueprint

from env import *

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

from controllers.IndexController import IndexController


class AuthController:
    def test_api_request():
        if 'credentials' not in flask.session:
            return flask.redirect('authorize')

        credentials = google.oauth2.credentials.Credentials(
            **flask.session['credentials'])

        drive = googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, credentials=credentials)

        files = drive.files().list().execute()
        flask.session['credentials'] = AuthController.credentials_to_dict(
            credentials)

        return flask.jsonify(**files)

    def credentials_to_dict(credentials):
        return {'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'client_id': credentials.client_id,
                'client_secret': credentials.client_secret,
                'scopes': credentials.scopes}

    def authorize():
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, scopes=SCOPES)

        flow.redirect_uri = flask.url_for(
            'drive_auth.oauth2callback', _external=True)

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')

        flask.session['state'] = state

        return flask.redirect(authorization_url)

    def oauth2callback():
        state = flask.session['state']

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES,
            state=state
        )

        flow.redirect_uri = flask.url_for(
            'drive_auth.oauth2callback', _external=True)

        authorization_response = flask.request.url
        flow.fetch_token(authorization_response=authorization_response)

        credentials = flow.credentials
        flask.session['credentials'] = AuthController.credentials_to_dict(
            credentials)

        return ('Authorization Successfully' + IndexController.index())

    def revoke():
        AuthController.check()

        credentials = google.oauth2.credentials.Credentials(
            **flask.session['credentials'])

        revoke = requests.post('https://oauth2.googleapis.com/revoke',
                               params={'token': credentials.token},
                               headers={'content-type': 'application/x-www-form-urlencoded'})

        status_code = getattr(revoke, 'status_code')

        if status_code == 200:
            return ('Credentials successfully revoked.' + IndexController.index())
        else:
            return ('An error occurred.' + IndexController.index())

    def clear_credentials():
        if 'credentials' in flask.session:
            del flask.session['credentials']

        return ('Credentials have been cleared.' + IndexController.index())

    def check():
        if 'credentials' not in flask.session:
            return ('You need to <a href="/authorize">authorize</a> before ' +
                    'testing the code to revoke credentials.')

    def get_credentials():
        return google.oauth2.credentials.Credentials(
            **flask.session['credentials'])

    def get_drive_service():
        credentials = AuthController.get_credentials()

        return googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, credentials=credentials)
