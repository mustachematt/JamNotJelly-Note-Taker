from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.email import send_password_reset_email
from app.forms import AccountForm, LoginForm, NoteForm, NoteDeleteForm
from app.forms import RegistrationForm, ResetPasswordForm, ResetPasswordRequestForm
from flask_login import current_user, login_required, login_user, logout_user
from app.models import Note, User
from werkzeug.urls import url_parse


@app.route('/', methods=['GET','POST'])
@app.route('/homepage', methods=['GET','POST'])
def homepage():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('mynotes')
        return redirect(url_for('mynotes'))
    return render_template('homepage.html', form=form)


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


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = AccountForm(current_user.username, current_user.email)
    if form.validate_on_submit():
        pw = request.form['password']
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data
        if pw != '':
            current_user.set_password(form.password.data)
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
    return render_template('account.html', form=form)


@app.route('/mynotes', methods=['GET', 'POST'])
@login_required
def mynotes():
    form = NoteForm()
    noteID = request.args.get('noteID')
    #if creating a new note
    if form.validate_on_submit() and noteID is None:
        if 'submit' in request.form:
            note = Note(body=form.note.data, due_date=form.due_date.data, author=current_user)
            db.session.add(note)
            db.session.commit()
        return redirect(url_for('mynotes'))
    notes = current_user.get_notes().all()
    #update existing note
    noteData = Note.query.filter_by(id=noteID).first()
    if form.validate_on_submit() and noteID is not None:
        if 'submit' in request.form:
            noteData.body = form.note.data
            noteData.due_date = form.due_date.data
            noteData.author = current_user
            db.session.commit()
        return redirect(url_for('mynotes'))
    #if editing a note, do the following. Will not run if submitting a new note
    if noteID is not None:
        form.note.data = noteData.body
        form.due_date.data = noteData.due_date
    #display note to edit
    return render_template('mynotes.html', form=form, notes=notes)


@app.route('/delete-notes', methods=['GET', 'POST'])
@login_required
def delete_note():
    form = NoteDeleteForm()
    if form.is_submitted():
        if 'submit' in request.form:
            note = Note.query.filter_by(user_id=current_user.id)
            for n in note:
                db.session.delete(n)
                db.session.commit()
        if 'submitSingle' in request.form:
            singleID = int(request.form['submitSingle'])
            note = Note.query.filter_by(id=singleID).first()
            db.session.delete(note)
            db.session.commit()
            if Note.query.filter_by(user_id=current_user.id).first() is not None:   
                return redirect(url_for('delete_note'))
        return redirect(url_for('mynotes'))
    notes = current_user.get_notes().all()
    return render_template('delete-notes.html', form=form, notes=notes)


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
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('mynotes')
        return redirect(url_for('mynotes'))
    return render_template('register.html', form=form)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('mynotes'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('mynotes'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('homepage'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/design')
def design():
    return render_template('/static/design.css')
