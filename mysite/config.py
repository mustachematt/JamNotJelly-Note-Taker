import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # install flask-wtf ext. The ext uses this to protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # install flask-sqlalchemy and flask-migrate
    # sqllchemy is an ORM that creates/executes db code for our sqlite app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False