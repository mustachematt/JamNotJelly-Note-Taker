from app.models import Note, User
from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class NoteForm(FlaskForm):
    note = TextAreaField(validators=[DataRequired()])
    due_date = DateField('Due Date', format='%m/%d/%Y', validators=[Optional()])
    submit = SubmitField('Save')

    def validate_due_date(self, due_date):
        note = Note.query.filter_by(due_date=due_date.data).first()
        if note is not None:
            raise ValidationError('Enter date as mm/dd/yyyy')