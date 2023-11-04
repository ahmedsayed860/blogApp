from flask import Blueprint, render_template, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegisterForm, LoginForm
from .models import Users
from blog import db
from flask_login import login_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		username = form.username.data
		email = form.email.data
		passwd_hash = generate_password_hash(form.password.data)
		user = Users(username=username, email=email, password_hash=passwd_hash)
		db.session.add(user)
		db.session.commit()
		flash('Your registeration is successful', 'success')
		return redirect(url_for('index'))
	return render_template('auth/register.html', form=form, title='Sign In')


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user and check_password_hash(user.password, form.password.data):
			login_user(user)
			return redirect(url_for('index'))
		else :
			flash('Login unsuccessful, try agin.', 'danger')
	return render_template('auth/login.html', form=form, title='Sign In')
