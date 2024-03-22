#!/usr/bin/python3
""" Flask web_app module"""
from flask import Flask, render_template
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
@web_app.route("/python/<text>", strict_slashes=False)
def python_cool(text="is cool"):
    """Function to return Python + text in the url after /python/"""
    text = text.replace("_", " ")
    return f'Python {text}'


@web_app.route("/number/<n>", strict_slashes=False)
def check_num(n):
    """Function to return number in the url after /number/"""
    if isinstance(n, int):
        return f'{n} is a number'


@web_app.route("/number_template/<n>", strict_slashes=False)
def check_num_temp(n):
    """Function to return number in the url after /number/"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@web_app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """Function to return number in the url after /number/"""
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template("6-number_odd_or_even.html",
                                   n=n, num_type='even')
        else:
            return render_template("6-number_odd_or_even.html",
                                   n=n, num_type='odd')


if __name__ == "__main__":
    web_app.run()
