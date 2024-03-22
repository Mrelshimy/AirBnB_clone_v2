#!/usr/bin/python3
""" Flask web_app module"""
from flask import Flask
web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == "__main__":
    web_app.run()
