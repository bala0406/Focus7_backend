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
    SQLALCHEMY_DATABASE_URI = "postgres://lstplxgnurplcj:675c3ad9a7fa1fd2c7aef0246575de8d0f4c03bdc96e44ec695425d9e76ab312@ec2-34-197-212-240.compute-1.amazonaws.com:5432/dfr4p8u6g53kvk"
    SECRET_KEY = "ba094042e2e58bc968182c7b00c58dc3"
    
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
