"""
    Title: Building a Python Websever
    Purpose: To build a webserver in Python
    Author: Crystal Quick
    Reference: https://projects.raspberrypi.org/en/projects/python-web-server-with-flask
"""

from flask import Flask, render_template

app = Flask(__name__)

""" Creating a new route and page called index. """
@app.route('/')
def index():
    return render_template('index.html')

""" Creating a new route and page called cakes. """
@app.route('/cakes')
def cakes():
     return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')