from app import db, login
import pytz
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# these are the classes (database models)
# SQLAlchemy handles the db translations of these classes into tables
# and objects into rows

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    notes = db.relationship('Note', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_notes(self):
        return Note.query.filter(Note.user_id == self.id).order_by(
            Note.timestamp.desc())

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    universalTime = datetime.datetime.utcnow()
    #timezone can be changed
    timezone = pytz.timezone("US/Eastern")
    localizedTime = pytz.utc.localize(universalTime)
    timeToDisplay = localizedTime.astimezone(timezone)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=timeToDisplay)
    due_date = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Note {}>'.format(self.body)
