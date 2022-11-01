from flask import Blueprint, request, session
from flask import jsonify
from app.dao.auth.UserDao import UserDao
from handler.factory import ResponseFactory
from app.middleware.Jwt import UserToken
from flask import render_template

auth = Blueprint("auth",__name__,url_prefix='/auth')

#这里以auth.route注册的函数都会自带/auth,所以url是/auth/register
@auth.route("/register",methods=["POST"])
def register():
    #获取request请求数据

    print(request.data)
    data = request.get_json()
    print(data)
    username,password = data.get("username"),data.get("password")
    if not username or not password:
        return jsonify(dict(code=101,msg="用户名或密码不能为空"))
    email, name = data.get("email"), data.get("name")
    if not email or not name:
        return jsonify(dict(code=101,msg="姓名或邮箱不能为空"))

    err = UserDao.register_user(username,name,password,email)
    if err is not None:
        return jsonify(dict(code=110,msg=err))
    return jsonify(dict(code=0,msg="注册成功"))

@auth.route("/login",methods=["POST"])
def login():
    print(request.headers)
    #标识通过什么登录，0为页面，1为接口
    flag = 0
    username, password = "",""
    #通过接口登录
    data = request.get_json()
    if data is not None:
        username,password = data.get("username"),data.get("password")
        flag = 1
    else:
        #通过 前端页面登录
        username,password = request.form["username"],request.form["password"]
    print(username,password)
    if not username or not password:
        return jsonify(dict(code=101,msg="用户名或密码不能为空"))
    user,err = UserDao.login(username,password)

    if err is not None:
        return jsonify(dict(code=110,msg=err))

    user = ResponseFactory.model_to_dict(user,"password")
    token = UserToken.get_token(user)
    if err is not None:
        return jsonify(dict(code=110,msg=err))

    session["token"] = token
    if flag == 1:
        return jsonify(dict(code=0,msg="登录成功",data=dict(token=token,user=user)))
    else:
        return render_template("index.html")