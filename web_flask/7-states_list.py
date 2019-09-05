#!/usr/bin/python3
"""
Script that starts a Flask web application:
web application must be listening on 0.0.0.0, port 5000

"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Flask will automatically remove database sessions
    at the end of the request
    or when the application shuts down"""
    storage.close()


@app.route('/states_list')
def states_list():
    """display a HTML page: (inside the tag BODY)
    H1 tag: States
    UL tag: with the list of all State objects present in DBStorage
    sorted by name (A->Z)"""
    states_list = []
    states_list = list(storage.all().values())
    return render_template('7-states_list.html', state=states_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
