#!/usr/bin/python3
"""implement the forth routing"""
from flask import Flask, render_template

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
    return "c {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_txt_with_def(text='is cool'):
    """displaying the text with default"""
    return "Python  {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def only_int(n):
    """displays it only if it's a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def first_template(n):
    """render the first template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0',  port=5000)
