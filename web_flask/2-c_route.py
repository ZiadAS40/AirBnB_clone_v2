#!/usr/bin/python3
"""implement the third routing"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """just HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_txt(text):
    """displaying the text"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0',  port=5000)
