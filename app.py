#NOTE
'''
All objects created are imported to app.py file
While Using Command Line, import the packages,classes and methods only from app.py file
Don't import from specific files or packages except app.py, you will get an circular import error
For most cases use the commands created with flask_manager in manage.py file
'''
#NOTE
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

@app.route("/")
def home():
    return "use /getquestions for api and /admin for admin interface"

# if __name__ == '__main__':
#     app.run()
