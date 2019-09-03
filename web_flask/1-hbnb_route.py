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
def display_hello_hbnb():
    """ return Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def diplay_hbnb():
    """ return HBNB """
    return 'HBNB'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
