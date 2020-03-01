from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
