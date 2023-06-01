import os
import flask
from routes import blueprint

app = flask.Flask(__name__)
app.secret_key = 'fh4t729eufh2948hsj29'

app.register_blueprint(blueprint)

if __name__ == '__main__':
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  app.run('0.0.0.0', 8006, debug=True)