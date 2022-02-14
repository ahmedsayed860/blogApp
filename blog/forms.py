from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('email', validators=[DataRequired()])
    passwd = PasswordField(
        'Mot de passe', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm_passwd = PasswordField('Confirmez votre mot de passe',
                                   validators=[DataRequired()])
    submit = SubmitField('S\'enregistrer')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    passwd = PasswordField('Mot de passe',
                           validators=[DataRequired(),
                                       EqualTo('confirm',
                                               message='Passwords must match')])
    submit = SubmitField('S\'enregistrer')
