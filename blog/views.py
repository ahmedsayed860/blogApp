from flask import render_template
from blog import app
from blog.forms import RegisterForm, LoginForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
