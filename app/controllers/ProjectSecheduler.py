from datetime import datetime

from flask import render_template
from flask import request, session, redirect, Blueprint

from app.models import db
from app.models.project import Project
from app.models.project_scheduler import ProjectScheduler
from app.utils.SchedulerUtil import scheduler, execute_cases_by_project_id
from app.utils.SingletonDecorator import permission
from app.utils.logger import Log

project_scheduler = Blueprint("project_scheduler",__name__,url_prefix='/project_scheduler')


log = Log("ProjectSecheduler")

#进入定时任务管理列表页面
@project_scheduler.route('/list',methods = ['POST','GET'])
def to_list():
    sign = request.args.get('sign')
    if sign is not None:
        session['sign'] = sign

    project_schedulers = ProjectScheduler.query.filter(ProjectScheduler.deleted_at == None)

    return render_template('project-scheduler/project-scheduler.html',project_schedulers=project_schedulers)


@project_scheduler.route('/to_add',methods = ['GET'])
def to_add():
    projects = Project.query.filter(Project.deleted_at == None).all()
    return render_template('project-scheduler/project-scheduler-add.html',projects=projects)


@project_scheduler.route('/add',methods = ['POST'])
@permission()
def add(user_info):
    project_id = request.form['project_id']
    name = request.form['name']
    rule = request.form['rule']


    p = Project.query.get(project_id)
    # 插入数据
    wait_add_project_scheduler = ProjectScheduler(project_id, p.name, name, user_info.get('id'), user_info.get('name'),
                                                  'cron', rule)
    db.session.add(wait_add_project_scheduler)
    db.session.commit()



    #添加定时任务
    rules = rule.split(' ')
    scheduler.add_job(func=execute_cases_by_project_id, args=(project_id, wait_add_project_scheduler.id),
                      id=wait_add_project_scheduler.ps_id, trigger='cron', second=rules[0], minute=rules[1],
                      hour=rules[2], day=rules[3], month=rules[4], week=rules[5])


    return redirect('list')


@project_scheduler.route('/to_edit',methods = ['POST','GET'])
def to_edit():
    id = request.args.get("id")
    project_scheduler = ProjectScheduler.query.filter_by(id=id).first()
    projects = Project.query.filter(Project.deleted_at == None).all()

    return render_template('project-scheduler/project-scheduler-edit.html',project_scheduler=project_scheduler,projects=projects)

@project_scheduler.route('/edit',methods = ['POST','GET'])
def edit():
    id = request.form['id']
    project_id = request.form['project_id']
    name = request.form['name']
    rule = request.form['rule']

    p = Project.query.get(project_id)

    edit_scheduler = ProjectScheduler.query.get(id)
    edit_scheduler.project_id = project_id
    edit_scheduler.project_name = p.name
    edit_scheduler.rule = rule
    edit_scheduler.name = name
    edit_scheduler.updated_at = datetime.now()
    edit_scheduler.execute_count = 0
    db.session.commit()

    rules = rule.split(' ')


    #先删除定时任务
    try:
        scheduler.delete_job(edit_scheduler.ps_id)
    except Exception as e:
        log.error(f'删除定时任务时出错：str(e)')

    #再添加定时任务
    scheduler.add_job(func=execute_cases_by_project_id, args=(project_id, edit_scheduler.id),
                      id=edit_scheduler.ps_id, trigger='cron', second=rules[0], minute=rules[1],
                      hour=rules[2], day=rules[3], month=rules[4], week=rules[5])


    return redirect('list')


#暂停定时任务
@project_scheduler.route('/stop',methods = ['POST','GET'])
def stop():
    id = request.args.get("id")
    project_scheduler = ProjectScheduler.query.filter_by(id=id).first()
    project_scheduler.status = '2'
    db.session.commit()

    #暂停定时任务
    try:
        scheduler.pause_job(project_scheduler.ps_id)
    except Exception as e:
        log.error(f"暂停定时任务：str(e)")

    return redirect('list')


#恢复定时任务
@project_scheduler.route('/resume',methods = ['POST','GET'])
def resume():
    id = request.args.get("id")
    project_scheduler = ProjectScheduler.query.filter_by(id=id).first()
    project_scheduler.status = '1'
    db.session.commit()

    #恢复定时任务
    try:
        scheduler.resume_job(project_scheduler.ps_id)
    except Exception as e:
        log.error(f"恢复定时任务：str(e)")

    return redirect('list')


@project_scheduler.route('/delete',methods = ['GET'])
def delete():
    id = request.args.get("id")
    project_scheduler = ProjectScheduler.query.get(id)
    project_scheduler.deleted_at = datetime.now()
    project_scheduler.status = '0'

    db.session.commit()

    # 删除定时任务
    try:
        scheduler.delete_job(project_scheduler.ps_id)
    except Exception as e:
        log.error(f"删除定时任务：str(e)")

    return redirect('list')
