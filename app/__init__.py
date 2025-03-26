from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Setup Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Import routes (after app & db to avoid circular imports)
from app import routes
