from routes.drive_auth import drive_auth
from routes.drive import drive
import os
import flask
import requests

app = flask.Flask(__name__)
app.secret_key = 'hf1389G*38g08FG782g1348'


app.register_blueprint(drive)
app.register_blueprint(drive_auth)

if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Https Verification
    app.run(debug=True, port=8006, host='0.0.0.0')
