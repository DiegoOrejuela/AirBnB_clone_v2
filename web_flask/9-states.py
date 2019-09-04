#!/usr/bin/python3
"""Module 9-states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states/', defaults={"id": None})
@app.route('/states/<id>')
def cities_by_states(id):
    """display a HTML page: (inside the tag BODY)
    - If a State object is found with this id:
    *H1 tag: “State: ”
    *H3 tag: “Cities:”
    *UL tag: with the list of City objects linked to the State sorted by name
    (A->Z)
    **LI tag: description of one City: <city.id>: <B><city.name></B>
    - Otherwise:
    *H1 tag: “Not found!”
    """
    dict_state = storage.all("State")
    if id:
        state = dict_state.get("State." + id)
        return render_template("9-states.html", states=None, state=state)
    else:
        objects = list(dict_state.values())
        objects.sort(key=lambda x: x.name)
        return render_template("9-states.html", states=objects, state=None)


@app.route('/states_list')
def states_list():
    """states_list - display a HTML page: (inside the tag BODY)
    H1 tag: 'States' | UL tag: with the list of all State objects present
    in DBStorage sorted by name (A->Z) tip | LI tag: description of
    one State"""

    objects = list(storage.all("State").values())
    objects.sort(key=lambda x: x.name)
    return render_template("8-cities_by_states.html", objects=objects)


@app.teardown_appcontext
def shutdown_session(exception=None):
    "close the session"
    storage.close()


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """number_odd_or_even - display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    Return: HTML with format"""

    return render_template("6-number_odd_or_even.html", n=n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """number - display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    Return: HTML with format"""

    return render_template("5-number.html", n=n)


@app.route('/number/<int:n>')
def number(n):
    """number - display “n is a number” only if n is an integer
    Return: string with format"""

    return "{} is a number".format(n)


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
