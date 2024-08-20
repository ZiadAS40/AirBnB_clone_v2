#!/usr/bin/python3
"""state routing"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """return html consit of state list"""

    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html',
                           states=states)


@app.teardown_appcontext
def close(exception=None):
    """tear down after session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
