from flask import Flask

#create a flask app instance
app = Flask(__name__)

#create route and test function
@app.route('/')
def hello_world():
    return 'Hello world'
def my_name:
    return input("yo name")