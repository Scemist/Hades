import flask
import requests
from flask import render_template
from flask import Blueprint

from drive_config import *

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

from controllers.IndexController import IndexController


class AuthController:
    def credentials_to_dict(credentials):
        return {'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'client_id': credentials.client_id,
                'client_secret': credentials.client_secret,
                'scopes': credentials.scopes}

    def get_user_info(): # User object
        drive = AuthController.get_drive_service()
        response = drive.about().get(fields="user").execute()
        return response["user"]

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

        flask.session['user'] = AuthController.get_user_info()
        flask.flash('Authorization Successfully.')
        return flask.redirect('/')

    def revoke():
        if not AuthController.check():
            flask.flash('Already revoked.')

            return flask.redirect('/')

        credentials = AuthController.get_credentials()

        revoke = requests.post('https://oauth2.googleapis.com/revoke',
                               params={'token': credentials.token},
                               headers={'content-type': 'application/x-www-form-urlencoded'})

        status_code = getattr(revoke, 'status_code')

        if status_code == 200:
            flask.flash('Credentials successfully revoked.')
            return IndexController.index()
        else:
            flask.flash('An error occurred.')
            return IndexController.index()

    def clear_credentials():
        if 'credentials' in flask.session:
            del flask.session['credentials']

        AuthController.revoke()
        if 'credentials' in flask.session:
            del flask.session['key']

        flask.session.clear()

        flask.flash('Credentials have been cleared.')

        return IndexController.index()

    def check():
        try:
            if 'credentials' not in flask.session:
                return False

            credentials = google.oauth2.credentials.Credentials(
                **flask.session['credentials'])

            return True
        except (KeyError, IndexError):
            return False

    def get_credentials():
        return google.oauth2.credentials.Credentials(
            **flask.session['credentials'])

    def get_drive_service():
        credentials = AuthController.get_credentials()

        return googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, credentials=credentials)

    def set_key(key):
        flask.session['key'] = key

        flask.flash('Key setted successfully.')
        return flask.redirect('/files')

    def destroy_key():
        del flask.session['key']

        flask.flash('Key deleted successfully.')
        return flask.redirect('/')
