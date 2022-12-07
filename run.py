
from app import better
from app.models import db
from app.models.job import Job
from app.utils.logger import Log
from app import dao
from app.controllers.auth.user import auth
from app.controllers.project.project import pr
from app.controllers.request.http import req
from app.controllers.user.user import user
from app.controllers.user.role import role
from app.controllers.project.projectRole import projectRole
from app.controllers.case.case import case
from app.controllers.database.dataBase import database
from app.controllers.redis.redis import rediss
from app.controllers.job.job import job
from flask import render_template
from app.controllers.ssh import ssh
from app.utils.SchedulerUtil import scheduler
from app.controllers.ProjectSecheduler import project_scheduler


#注册蓝图
better.register_blueprint(auth)
better.register_blueprint(req)
better.register_blueprint(pr)
better.register_blueprint(user)
better.register_blueprint(role)
better.register_blueprint(projectRole)
better.register_blueprint(case)
better.register_blueprint(database)
better.register_blueprint(rediss)
better.register_blueprint(job)
better.register_blueprint(ssh)
better.register_blueprint(project_scheduler)


import sys
sys.path.append('./')

#定时任务
scheduler.init_app(better)
scheduler.start()
#将数据库中状态为1的任务添加到定时任务中，因为重启会清空
from app.controllers.ProjectSecheduler import ProjectScheduler
from app.utils.SchedulerUtil import execute_cases_by_project_id

projectSchedulers = ProjectScheduler.query.filter(ProjectScheduler.status != '0',ProjectScheduler.deleted_at == None).all()
#先全部启动
for projectScheduler in projectSchedulers:
    rules = projectScheduler.rule.split(' ')

    scheduler.add_job(func=execute_cases_by_project_id, args=(projectScheduler.project_id,projectScheduler.id),id=projectScheduler.ps_id, trigger='cron', second=rules[0], minute=rules[1],
                      hour=rules[2], day=rules[3], month=rules[4], week=rules[5])
    #为暂停状态的暂停
    if projectScheduler.status == '2':
        scheduler.pause_job(projectScheduler.ps_id)




@better.route('/')
def login_page():
    log = Log("hello world 专用")
    log.info("有人访问了登录页面")
    return render_template('login.html')

if __name__ == "__main__":
    better.config['JSON_AS_ASCII'] = False
    better.run("0.0.0.0",threaded=True,port="7788")