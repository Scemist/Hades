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

blueprint = Blueprint("app", __name__)

@blueprint.route('/')
def index():
	return IndexController.index()

@blueprint.route('/test')
def test_api_request():
	return AuthController.test_api_request()

@blueprint.route('/authorize')
def authorize():
	return AuthController.authorize()

@blueprint.route('/oauth2callback')
def oauth2callback():
	return AuthController.oauth2callback()


@blueprint.route('/revoke')
def revoke():
	return AuthController.revoke()


@blueprint.route('/clear')
def clear_credentials():
	return AuthController.clear_credentials()