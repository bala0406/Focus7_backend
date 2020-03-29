
############################################################
import os
from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
############################################################
from main import app
from main import db
############################################################

app.config.from_object("config.DevelopmentConfig")

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()
