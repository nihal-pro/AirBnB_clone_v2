#!/usr/bin/python3
"""this script starts a Flask web application
    this web application must be listening on 0.0.0.0 at port 5000
    Route:
        /cities_by_states: ***
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states/cites
        at '/cities_by_states' path
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
