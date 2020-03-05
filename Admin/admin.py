############################################################
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
############################################################
from app import app
from app import db
from Models.models import Question
from Models.adminmodel import Administrator
###########################################################

# @login.loadUser
# def loadUser(admin_id):
#     return Administrator.query.get(admin_id)

class ModelView(ModelView):
    column_display_pk = True

    # def is_accessible(self):
    #     # return current_user.is_autheticated
    #     pass

# @app.route("/login")
# def login():
#     user = Administrator.query.get(1)
#     login_user(user)
#     return "Logged in"

# def logout():
#     logout_user()
#     return "Logged out"


admin = Admin(app)
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(Administrator, db.session))
