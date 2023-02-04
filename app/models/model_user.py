from .entities.user import User
from .entities.user_access import UserAccess

class ModelUser:

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            query = "SELECT idUser, userName, userPass FROM user WHERE userName='{0}'".format(user.userName)
            cursor.execute(query)
            data = cursor.fetchone()
            if data != None:
                fits = User.check_user(data[2], user.userPass)
                if fits:
                    user_logged= User(data[0], data[1], None, None)
                    return user_logged
                else:
                    return None
            else:
                return None
        except Exception as e:
            raise Exception(e)


    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = """SELECT user.idUser, user.userName, user_access.idUserAccess, user_access.accessType
                        FROM user 
                        JOIN user_access 
                        ON user.idUserAccess = user_access.idUserAccess 
                        WHERE user.idUser = {0}""".format(id)
            cursor.execute(query)
            data = cursor.fetchone()
            user_permission = UserAccess(data[2], data[3])
            logged_user = User(data[0], data[1], None, user_permission)
            return logged_user
        except Exception as e:
            raise Exception(e)