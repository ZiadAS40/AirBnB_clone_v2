#!/usr/bin/python3
"""implement the second routing"""
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


if __name__ == "__main__":
    app.run(host='0.0.0.0',  port=5000)
