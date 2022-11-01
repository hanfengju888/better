from functools import wraps
from flask import request,jsonify,session
from app import better
from app.middleware.Jwt import UserToken

FORBIDDENT = "对不起，你没有足够权限"

class SingletonDecorator:
    def __init__(self,cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args,**kwargs)
        return self.instance

def permission(role="GUEST"):
    role=better.config.get(role,0)
    def login_required(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            try:
                token = session.get("token")
                if token is None:
                    return jsonify(dict(code=401,msg="用户信息认证失败，请检查"))
                user_info = UserToken.parse_toekn(token)
                #信息写入kwargs
                kwargs["user_info"] = user_info
            except Exception as e:
                return jsonify(dict(code=401,msg=str(e)))
            #判断用户权限是否足够，不足够直接返回不继续
            if user_info.get("role",0) < role:
                return jsonify(dict(code=400,mgs=FORBIDDENT))
            return func(*args,**kwargs)

        return wrapper
    return login_required