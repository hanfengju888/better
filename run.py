from app import better
from app.utils.logger import Log
from app import dao
from app.controllers.auth.user import auth

#注册蓝图
better.register_blueprint(auth)


@better.route('/')
def hello_world():
    log = Log("hello world 专用")
    log.info("有人访问了")
    return 'hello world!'

if __name__ == "__main__":
    better.config['JSON_AS_ASCII'] = False
    better.run("0.0.0.0",threaded=True,port="7777")