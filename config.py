############################################################
import os
############################################################

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("FOCUS7_FLASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("FOCUS7_SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgres://mtvjyykijbejqz:52df3302a3c23d8f444fbce42996988421315657eb3ec8fbe1b99bf7328bc9a5@ec2-52-207-93-32.compute-1.amazonaws.com:5432/degckucv04ef9e"

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True  
    TESTING = True     

class TestingConfig(Config):
    DEBUG = False
    TESTING = True    
