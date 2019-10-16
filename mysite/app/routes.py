from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/mynotes')
def mynotes():
    return render_template('mynotes.html')


@app.route('/design')
def design():
    return render_template('/static/design.css')
