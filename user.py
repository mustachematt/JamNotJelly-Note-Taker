class User:
    #this user class only contains the username and password
    #can be updated to fit our needs as the project grows 
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return "User('{}', '{}')".format(self.username, self.password)