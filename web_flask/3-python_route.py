#!/usr/bin/python3
"""
Script that starts a Flask web application:
web application must be listening on 0.0.0.0, port 5000
/: display Hello HBNB!
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """ return Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """ return HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """ return c followed by the value of the text variable """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text="is cool"):
    """ return Python , followed by the value of the text variable """
    return "Python {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
