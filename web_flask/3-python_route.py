#!/usr/bin/python3
""" Flask web_app module"""
from flask import Flask
web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Function to return Hello HBNB on root page"""
    return 'Hello HBNB!'


@web_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Function to return HBNB at /hbnb route"""
    return 'HBNB'


@web_app.route("/c/<string:text>", strict_slashes=False)
def c_fun(text):
    """Function to return C + text in the url after /c/"""
    text = text.replace("_", " ")
    return f'C {text}'


@web_app.route("/python", strict_slashes=False)
@web_app.route("/python/<string:text>", strict_slashes=False)
def python_cool(text="is cool"):
    """Function to return Python + text in the url after /python/"""
    text = text.replace("_", " ")
    return f'Python {text}'


if __name__ == "__main__":
    web_app.run()
