'''from flask_login import UserMixin

class User(UserMixin, db.Model):'''


class User:
    #this user class only contains the username and password
    #can be updated to fit our needs as the project grows 
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.username, self.email, self.password)