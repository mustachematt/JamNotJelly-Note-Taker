
from app.models import Note, User
from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, PasswordField, StringField
from wtforms import SubmitField, TextAreaField, HiddenField, SelectField
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
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already in use. Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('That email address is already in use. Please use a different email address.')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
    
class NoteForm(FlaskForm):
    note = TextAreaField(validators=[DataRequired()]) #body
    due_date = DateField('Due Date', format='%m/%d/%Y', validators=[Optional()])
    priorityLevel = SelectField('Priority', choices=[(0,'None'),(1,'Low'),(2,'Medium'),(3,'High')], coerce=int)
    submit = SubmitField('Save')
    def validate_due_date(self, due_date):
        note = Note.query.filter_by(due_date=due_date.data).first()
        if note is not None:
            raise ValidationError('Enter date as mm/dd/yyyy')
    title = StringField(validators=[Optional()])

class NoteDeleteForm(FlaskForm):
    note = TextAreaField(validators=[DataRequired()]) 
    due_date = DateField('Due Date', format='%m/%d/%Y', validators=[Optional()])
    submit = SubmitField('Delete All Notes', id='deleteAll')
    hiddenID = HiddenField('note')
    submitSingle = SubmitField()

class AccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=140)])
    password = PasswordField('Password')
    submit = SubmitField('Submit')

    def __init__(self, original_username, original_email, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Username already in use. Please use a different username.')

    def validate_email(self, email):
        if email.data != self.original_email:
            user = User.query.filter_by(email=self.email.data).first()
            if user is not None:
                raise ValidationError('That email address is already in use. Please use a different email address.')
