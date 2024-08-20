#!/usr/bin/python3
"""state routing"""
from flask import Flask, render_template
from models import storage, storage_ident
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_state_list():
    """return html consit of city by it's state"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    cities = sorted(list(storage.all("City").values()), key=lambda x: x.name)
    final_dict = {}
    if storage_ident == 'db':
        for state in states:
            city_list = []
            for city in cities:
                if city.state_id == state.id:
                    city_list.append(city)
            final_dict.update({state: city_list})
    else:
        for state in states:
            final_dict.update({state: [state.cities]})

    return render_template('7-states_list.html',
                           states=final_dict)


@app.teardown_appcontext
def close(exception=None):
    """tear down after session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
