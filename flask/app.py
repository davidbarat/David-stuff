
from flask import Flask
import io
import random
from flask import Response
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

if __name__ == "__main__":
    app.run()
