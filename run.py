from app import better
from app.utils.logger import Log
from app import dao
from app.controllers.auth.user import auth
from app.controllers.project.project import pr
from app.controllers.request.http import req
from app.controllers.user.user import user
from app.controllers.user.role import role
from app.controllers.project.projectRole import projectRole

from flask import render_template

#注册蓝图
better.register_blueprint(auth)
better.register_blueprint(req)
better.register_blueprint(pr)
better.register_blueprint(user)
better.register_blueprint(role)
better.register_blueprint(projectRole)


import sys
sys.path.append('./')

@better.route('/')
def login_page():
    log = Log("hello world 专用")
    log.info("有人访问了登录页面")
    return render_template('login.html')

if __name__ == "__main__":
    better.config['JSON_AS_ASCII'] = False
    better.run("0.0.0.0",threaded=True,port="7788")