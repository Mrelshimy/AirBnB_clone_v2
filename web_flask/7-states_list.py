#!/usr/bin/python3
""" Flask web_app module"""
from flask import Flask, render_template
from models import storage
from models.state import State
web_app = Flask(__name__)


@web_app.route("/states_list", strict_slashes=False)
def show_states():
    """ Function to return list of states"""
    states = storage.all(State)
    return render_template("7-states_list.html",
                           states=states)


@web_app.teardown_appcontext
def teardown(self):
    """Funtion to remove current SQLalchemy session"""
    storage.close()


if __name__ == "__main__":
    web_app.run()
