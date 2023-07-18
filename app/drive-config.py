import os

CLIENT_SECRETS_FILE = "drive-client-secret.json"
SCOPES = [
	'https://www.googleapis.com/auth/drive.file',
	'https://www.googleapis.com/auth/drive.resource',
]
API_SERVICE_NAME = "drive"
API_VERSION = "v3"
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'