from flask import Flask
from blog.config import Config


app = Flask(__name__)
app.config.from_object(Config)

import blog.views
