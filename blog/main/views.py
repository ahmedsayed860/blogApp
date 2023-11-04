from flask import Blueprint, render_template, redirect, flash, url_for


main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html', title='Home Page')

