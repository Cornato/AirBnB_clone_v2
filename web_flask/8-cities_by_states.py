#!/usr/bin/python3
"""
start the web application using Flask
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    """lists states from database
    Returns:
        HTML
    """
    dict_states = storage.all(State)
    all_states = []
    for k, v in dict_states.items():
        all_states.append(v)
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def tear_down(self):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
