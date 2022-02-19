from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from blog.config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Database connection variable
dbase = SQLAlchemy(app)
migrate = Migrate(app, dbase)

import blog.views
