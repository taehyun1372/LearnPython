import secrets
import hashlib
import hmac

class Server:
    def __init__(self):
        print("Server")
        self.user_db = dict()
        self.session_db = dict()

    def sign_in(self, username, password):
        if not self.user_db.get(username, None):
            salt = secrets.token_bytes(16)
            print(f"salt is created {salt}")
            hash_password = hashlib.sha256(password.encode() + salt).digest()
            self.user_db[username] = User(hash_password, salt)
            print("A new user created")
        else:
            print("The same user exists!")

    def log_in(self, username, password):
        if user := self.user_db.get(username):
            salt = user.salt
            hash_password = user.hash_password
            if hash_password == hashlib.sha256(password.encode() + salt).digest():
                print("Loggged in")
                cookie = hashlib.sha256(f"user({username})".encode()).digest()
                secret_key = secrets.token_bytes(10)
                if not self.session_db.get(username):
                    session = Session(username, cookie, secret_key)
                    self.session_db[username] = session
                return session
            else:
                print("Invalid password try again!")
                return None
        else:
            print("Invalid username")
            return None

    def get_page(self, username, cookie, mac_tag):
        if session:= self.session_db.get(username):
            internal_tag = hmac.new(
                session.secret_key,
                session.cookie,
                hashlib.sha256
            ).digest()
            if internal_tag == mac_tag:
                return "page 1"
            else:
                print("Invalid MAC")
        else:
            return "Unable to identify session"

class User:
    def __init__(self, hash_password, salt):
        self.hash_password = hash_password
        self.salt = salt

class Session:
    def __init__(self, username:str, cookie, secret_key):
        self.username = username
        self.cookie = cookie
        self.secret_key = secret_key


if __name__ == "__main__":
    server = Server()
    server.sign_in("roy", "1234!")
    session = server.log_in("roy", "12344!")
    session = server.log_in("roy", "1234!")
    if session:
        mac_tag = tag = hmac.new(
            session.secret_key,
            session.cookie,
            hashlib.sha256
        ).digest()
        result = server.get_page(session.username, session.cookie, mac_tag)
        print(result)
