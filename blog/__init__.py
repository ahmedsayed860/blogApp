from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


bootstrap = Bootstrap5()
fontawesome = FontAwesome()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
	app = Flask(__name__)
	app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'Litera'
	app.config['SECRET_KEY'] = 'you-will-never-guess'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"


	# Init extension for the application
	fontawesome.init_app(app)
	bootstrap.init_app(app)
	db.init_app(app)
	migrate.init_app(app, db)
	login_manager.init_app(app)

	# Blueprint
	from .auth.views import auth as auth_bp
	app.register_blueprint(auth_bp)

	# index View
	@app.route('/')
	def index():
		return render_template("index.html")

	# db instance
	from blog.auth.models import Users

	#with app.app_context():
	#	db.create_all()

	return app