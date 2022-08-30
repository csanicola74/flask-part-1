# the below imports the Flask object from the flask package
from flask import Flask

# creating the Flask application instance and give it the name app
app = Flask(__name__)

# the decorator, @app.route, is being told with '/' that the function will respond to web requests for the URL '/'


@app.route('/')
# creates the 'index' page and the ability to navigate between pages
@app.route('/index/')
# creates the 'hello' function and then runs the phrase 'Hello, World!' through it
def hello():
    return '<h1>Hello, World!</h1>'

# creates an 'about' page and function and runs the phrase through it


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application made by Caroline Sanicola.</h3>'

# creates a 'contact' page and function and runs the phrase through it


@app.route('/contact/')
def contact():
    return '<h3>If you would like to contact us, please don\'t.</h3>'
