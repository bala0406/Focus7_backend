from app import app
from models import Question


@app.route("/")
def home():
    return "use /getquestions for api and /admin for admin interface"