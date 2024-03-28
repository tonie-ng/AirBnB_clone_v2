#!/usr/bin/python3
"""
script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Hello world route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """HBNB route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """C route"""
    param = text.replace("_", " ")
    return "C {}".format(param)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Python route"""
    param = text.replace("_", " ")
    return "Python {}".format(param)


@app.route("/number/<int:n>", strict_slashes=False)
def integer_route(n):
    """Integer route"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
