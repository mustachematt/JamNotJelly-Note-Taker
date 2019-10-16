import sqlite3
from mysite.user import User

connection = sqlite3.connect('user.db')

cur = connection.cursor()

# this code was usedto create the initial db
# may need readded/modified to add their actual lists
# cur.execute("""CREATE TABLE users (
#                 username text,
#                 email text,
#                 password text
#                 )""")

#takes in a memeber of the user class (which has a username and password), and inserts it into the database
def insert_user(userIn):
    with connection:
        cur.execute("INSERT INTO users VALUES (:username, :email, :password)", {'username': userIn.username, 
                    'email': userIn.email, 'password': userIn.password})

#takes in username and password and attempts to make a new user
#returns true if username was not taken and inserts it, returns false is it was taken
#will need to be updated with hashing of passwords (currently stores pw in plain text)
def register(username, email, password):
    with connection:
        #make sure there is not a user with that username
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if cur.fetchall() == []: #cursor will point to an empty array if that user doesnt exist
            newUser = User(username, email, password)
            insert_user(newUser)
            return True
        else:
            return False


#takes in a username and password. Returns true only if the password is correct
#will need to be updated with hashing of passwords
def login(username, password):
    with connection:
        #get info about that user
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if cur.fetchall()[0][1] == password: #index 0 gives the entry, index 1 accesses pw
            return True
        return False

#example code. The code bellow gives and example of how to interface with this class
# user1 = User("John Doe", "password")
# print(register(user1.username, user1.password)) #should return true in empty db, false if ran again
# print(register(user1.username, user1.password)) #should return false, inserting same user twice
# print(login(user1.username, user1.password)) #should return true


connection.commit()
connection.close()