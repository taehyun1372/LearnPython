import hashlib
import secrets

class PasswordDB():
    def __init__(self):
        self.password_db = dict()

    def new_user(self, user_name, password):
        if not self.password_db.get(user_name, None):
            salt = secrets.token_bytes(16)
            print(f"salt is created {salt}")
            hash_password = hashlib.sha256(password.encode() + salt).digest()
            self.password_db[user_name] = User(hash_password, salt)
            print("A new user created")
        else:
            print("The same user exists!")

    def log_in(self, user_name, password):
        if user := self.password_db.get(user_name):
            salt = user.salt
            hash_password = user.hash_password
            if hash_password == hashlib.sha256(password.encode() + salt).digest():
                print("Loggged in")
            else:
                print("Invalid password try again!")
        else:
            print("Invalid username")

class User:
    def __init__(self, hash_password, salt):
        self.hash_password = hash_password
        self.salt = salt


if __name__ == "__main__":
    print("Something")
    db = PasswordDB()
    db.new_user("roy", "1234")
    db.log_in("roy", "12345")
    db.log_in("roy1", "1234")
    db.log_in("roy", "1234")