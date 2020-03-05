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
