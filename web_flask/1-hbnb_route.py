#!/usr/bin/python3
"""
    script that starts Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello HBNB!'



@app.route('/hbnb')
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.url_map.strict_slashe = False
    app.run(host='0.0.0', port=5000)
