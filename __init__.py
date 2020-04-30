import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Flask Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_APP = 'wsgi.py'
    FLASK_DEBUG = 1

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app(test_config=None):
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create database tables for our data models

        return app