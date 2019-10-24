from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    return render_template('homepage.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')