#!/usr/bin/python3
"""state routing"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close(exception=None):
    """tear down after session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """return html consit of state list"""
    objs = storage.all("State")
    state_objs = {}
    for k, v in objs.items():
        temp = k.split('.')
        state_objs.update({v.name: temp[1]})
    return render_template('7-states_list.html',
                           states=state_objs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
