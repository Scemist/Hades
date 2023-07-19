from flask import Blueprint, redirect
from controllers.IndexController import IndexController
from controllers.AuthController import AuthController

drive_auth = Blueprint('drive_auth', __name__)


@drive_auth.route('/')
def index():
    return IndexController.index()


@drive_auth.route('/test')
def test_api_request():
    return AuthController.test_api_request()


@drive_auth.route('/authorize')
def authorize():
    return AuthController.authorize()


@drive_auth.route('/oauth2callback')
def oauth2callback():
    return AuthController.oauth2callback()


@drive_auth.route('/revoke')
def revoke():
    # if AuthController.check():
    #     return AuthController.check()
    # else:
    return AuthController.revoke()


@drive_auth.route('/clear')
def clear_credentials():
    return AuthController.clear_credentials()