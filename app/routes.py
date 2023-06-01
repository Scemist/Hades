import flask
import requests
from flask import render_template

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

from env import *
from flask import Blueprint

from controllers.IndexController import IndexController

blueprint = Blueprint("app", __name__)

@blueprint.route("/")
def index():
    return IndexController.index()

@blueprint.route("/test")
def test_api_request():
    if "credentials" not in flask.session:
        return flask.redirect("authorize")

    credentials = google.oauth2.credentials.Credentials(**flask.session["credentials"])

    drive = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )

    files = drive.files().list().execute()

    flask.session["credentials"] = credentials_to_dict(credentials)

    return flask.jsonify(**files)


@blueprint.route("/authorize")
def authorize():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES
    )

    flow.redirect_uri = flask.url_for("app.oauth2callback", _external=True)

    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )

    flask.session["state"] = state

    return flask.redirect(authorization_url)


@blueprint.route("/oauth2callback")
def oauth2callback():
    state = flask.session["state"]

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state
    )
    flow.redirect_uri = flask.url_for("app.oauth2callback", _external=True)

    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    flask.session["credentials"] = credentials_to_dict(credentials)

    return flask.redirect(flask.url_for("app.test_api_request"))


@blueprint.route("/revoke")
def revoke():
    if "credentials" not in flask.session:
        return (
            'You need to <a href="/authorize">authorize</a> before '
            + "testing the code to revoke credentials."
        )

    credentials = google.oauth2.credentials.Credentials(**flask.session["credentials"])

    revoke = requests.post(
        "https://oauth2.googleapis.com/revoke",
        params={"token": credentials.token},
        headers={"content-type": "application/x-www-form-urlencoded"},
    )

    status_code = getattr(revoke, "status_code")
    if status_code == 200:
        return "Credentials successfully revoked." + print_index_table()
    else:
        return "An error occurred." + print_index_table()


@blueprint.route("/clear")
def clear_credentials():
    if "credentials" in flask.session:
        del flask.session["credentials"]
    return "Credentials have been cleared.<br><br>" + print_index_table()


def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }
