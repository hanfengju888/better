import hashlib
from datetime import timedelta,datetime

import jwt
# from jwt.exceptions import ExpiredSignatureError
EXPIRD_HOUR = 3

class UserToken(object):
    key = 'betterToken'
    salt = 'better'

    @staticmethod
    def get_token(data):
        new_data = dict({'exp':datetime.utcnow() + timedelta(hours=EXPIRD_HOUR)},**data)
        return jwt.encode(new_data,key=UserToken.key)

    @staticmethod
    def parse_toekn(token):
        try:
            return jwt.decode(token,key=UserToken.key)
        except Exception:
            raise Exception("token已过期，请重新登录")

    @staticmethod
    def add_salt(password):
        m = hashlib.md5()
        m.update(f'{password}{UserToken.salt}'.encode('utf-8'))
        return m.hexdigest()