############################################################
from app import db
from flask_login import UserMixin
############################################################

class Administrator(db.Model,UserMixin):
    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(16), nullable=False)

    