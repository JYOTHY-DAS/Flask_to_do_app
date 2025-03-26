from flask import Flask #importing the Flask class from the flask module.
from flask_sqlalchemy import SQLAlchemy
import os

# Setup Flask app
# Flask(__name__) creates an instance of the Flask class.
app = Flask(__name__) #app is now a Flask application object that we can use to define routes, handle requests, etc.

# Configure SQLite database
'''
* Configures SQLAlchemy to use an SQLite database named todo.db 
* Three slashes mean relative path (database is in the project folder) '''

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# Prevents Flask-SQLAlchemy from tracking changes to objects to save memory.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
'''
* Creates a database connection linked to the Flask app.
* db will be used to define database models and interact with the database.'''

db = SQLAlchemy(app)

# Import routes (after app & db to avoid circular imports)
'''If we import routes at the beginning, routes.py might try to import app before it's fully created.
Importing it after app and db helps to avoids circular import issues.'''
from app import routes
