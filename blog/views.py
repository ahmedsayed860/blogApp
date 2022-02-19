from flask import render_template, redirect, url_for, flash
from blog import app, dbase
from blog.forms import RegisterForm, LoginForm
from blog.models import Users
from werkzeug.security import generate_password_hash#, check_password_hash


@app.route('/')
@app.route('/home')
def home():
    users = Users.query.all()
    return render_template('home.html', users=users)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.passwd.data
        user = Users(username=username, email=email,
                     passwd=generate_password_hash(password))
        dbase.session.add(user)
        dbase.session.commit()
        flash('success', 'Vous etes bien enregistrer!')
        return redirect(url_for('home'))
    """else:
        flash('danger', "Echec veuiller ressayer de vous enregister!")
        return redirect(url_for('register'))
    """
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
