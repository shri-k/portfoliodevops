from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to the Student System 9000!'

@app.route('/test')
def monk():
    return 'monkey donkey'