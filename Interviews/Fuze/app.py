from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

@app.route('/')
def index():
	return "Hello World!";


@app.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)



if __name__=='__main__':
	app.run(debug=True)