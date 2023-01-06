from blog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	password_hash = db.Column(db.String, nullable=False)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"