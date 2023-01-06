from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
	"""docstring for RegisterForm""", 
	username = StringField('Username', validators=[DataRequired()])
	email = EmailField('Email', validators=[Email(), DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(),
		EqualTo('confirm_password', message='Password must match')])
	confirm_password = PasswordField('Confirm Password')
	submit = SubmitField('Register')


class LoginForm(FlaskForm):
	"""docstring for LoginForm""", 
	email = EmailField('Email', validators=[Email(), DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log in')
