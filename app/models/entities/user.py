from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, idUser, userName, userPass, idUserAccess):
        self.idUser = idUser
        self.userName = userName
        self.userPass = userPass
        self.idUserAccess = idUserAccess

    
    def get_id(self):
        return self.idUser


    @classmethod
    def check_user(self, encripted, password):
        return check_password_hash(encripted, password)