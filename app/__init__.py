from flask import Flask
from views import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

@app.route('/')
def hello():
	return 'Hello world!'

if __name__ == '__main__':
	app.run(debug=True, port=8006, host='0.0.0.0')