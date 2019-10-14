from flask import render_template
from app import app
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/mynotes')
def mynotes():
    return render_template('mynotes.html')


@app.route('/design')
def design():
    return render_template('/static/design.css')
