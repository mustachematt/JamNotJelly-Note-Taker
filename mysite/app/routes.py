from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.forms import LoginForm, NoteForm, RegistrationForm
from flask_login import current_user, login_required, login_user, logout_user
from app.models import Note, User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('mynotes'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('mynotes')
        return redirect(url_for('mynotes'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/mynotes', methods=['GET', 'POST'])
@login_required
def mynotes():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(body=form.note.data, author=current_user)
        db.session.add(note)
        db.session.commit()
#        flash('Your note has been saved!')
        return redirect(url_for('mynotes'))
    notes = current_user.get_notes().all()
    return render_template('mynotes.html', form=form, notes=notes)

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('mynotes'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are a registered user! Login now!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/design')
def design():
    return render_template('/static/design.css')
