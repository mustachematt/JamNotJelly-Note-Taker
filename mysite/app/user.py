class User:
    #this user class can be updated to fit our needs as the project grows 
  
    def __init__(self, user_id, username, email, password_hash):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
    
    def __repr__(self):
        return "User('{}', '{}', '{}', '{}')".format(self.user_id, self.username, self.email, self.password_hash)

class Note:
    #this class houses the data associated with a user's note/post
    
    def __init__(self, note_id, body, timestamp, user_id):
        self.note_id = note_id
        self.body = body
        self.timestamp = timestamp
        self.user_id = user_id
    
    def __repr__(self):
        return "User('{}', '{}', '{}', '{}')".format(self.note_id, self.body, self.timestamp, self.user_id)