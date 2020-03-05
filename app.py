############################################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
############################################################

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)

############################################################
from Models.models import *
from api.Api import *
from Admin.admin import *
############################################################


if __name__ == '__main__':
    app.run()
