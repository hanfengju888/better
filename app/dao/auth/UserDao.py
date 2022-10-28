from sqlalchemy import or_
from app.middleware.Jwt import UserToken
from app.models import db
from app.models.user import User
from app.utils.logger import Log

class UserDao(object):
    log = Log("userDao")

    @staticmethod
    def register_user(username,name,password,email):
        try:
            users = User.query.filter(or_(User.username==username,User.email==email,User.name==name,User.password==password)).all()
            if users:
                raise Exception("用户名或邮箱已存在")
            #注册时密码加盐
            pwd = UserToken.add_salt(password)
            user = User(username,name,pwd,email)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            UserDao.log.error(f"用户注册失败:{str(e)}")
            return str(e)
        return None