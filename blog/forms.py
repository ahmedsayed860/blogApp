from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from blog.models import Users


class RegisterForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('email', validators=[DataRequired(), Email()])
    passwd = PasswordField('Mot de passe',
                           validators=[DataRequired(),
                                       EqualTo('confirm_passwd',
                                               message='Passwords must match')])
    confirm_passwd = PasswordField('Confirmez votre mot de passe',
                                   validators=[DataRequired()])
    submit = SubmitField('S\'enregistrer')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user == True:
            raise ValidationError("Ce nom d'utilisateur est deja utilise.")

    def validate_email(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user == True:
            raise ValidationError("Cet email est deja utilise.")


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    passwd = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')
