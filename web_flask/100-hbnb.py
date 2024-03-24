#!/usr/bin/python3
""" Flask web_app module"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
web_app = Flask(__name__)


@web_app.route("/hbnb", strict_slashes=False)
def show_filters():
    """ Function to return filters page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities,
                           places=places)


@web_app.teardown_appcontext
def teardown(self):
    """Funtion to remove current SQLalchemy session"""
    storage.close()


if __name__ == "__main__":
    web_app.run()
