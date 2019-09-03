#!/usr/bin/python3
"""Module 3-python_route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<string:text>')
def python(text):
    """python - display “Python ”, followed by the value of the text variable
    Return: string with format"""

    if "_" in text:
        text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/c/<string:text>')
def c(text):
    """c - display “C ” followed by the value of the text variable
    Return: string with format"""

    if "_" in text:
        text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/hbnb')
def HBNB():
    """HBNB - show acronym Holberton School
    Return: string 'HBNB'"""
    return 'HBNB'


@app.route('/')
def hello_HBNB():
    """hello_HBNB - say hello since Holberton School
    Return: string with greeting"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
