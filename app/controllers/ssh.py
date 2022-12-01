from flask import Flask,render_template,request,session,redirect,url_for,Blueprint
from flask import render_template
from datetime import datetime

from app.dao.project.ProjectRoleDao import ProjectRoleDao
from app.models import db
from app.models.role import Role
from app.models.ssh import Ssh
from app.utils.SshUtil import SSHLinux

ssh = Blueprint("ssh",__name__,url_prefix='/ssh')

#进入列表页
@ssh.route('/list',methods = ['POST','GET'])
def to_list():
    sign = request.args.get('sign')
    if sign is not None:
        session['sign'] = sign



    sshs = Ssh.query.filter(Ssh.deleted_at == None)
    for every in sshs:
        print(every.id)
        ssh = SSHLinux(every.ip, port=every.port, username=every.username, password=every.password)
        cpu_leave = ssh.use_command("vmstat|tail -1|awk '{print $(NF-2)}'")
        mem_info = ssh.use_command("""free -h|grep Me|awk '{print $2","$NF}'""")
        proecess_number = ssh.use_command("ps -ef|wc -l")

        mem_info = mem_info.strip().replace('G','').split(',')
        every.mem = str(round(float(mem_info[1])/float(mem_info[0])*100))
        every.cpu = cpu_leave.strip()
        every.process_number = proecess_number
        # db.session.commit()
    # sshs = Ssh.query.filter(Ssh.deleted_at == None)

    return render_template('ssh/ssh.html',sshs=sshs)


@ssh.route('/to_add',methods = ['GET'])
def to_add():

    return render_template('ssh/ssh-add.html')

@ssh.route('/add',methods = ['POST'])
def add():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    ip = request.form['ip']
    port = request.form['port']

    #插入数据
    wait_ssh = Ssh(name,ip,port,username,password)
    db.session.add(wait_ssh)
    db.session.commit()

    return redirect('list')


@ssh.route('/to_edit',methods = ['POST','GET'])
def to_edit():
    id = request.args.get("id")
    ssh = Ssh.query.filter_by(id=id).first()

    return render_template('ssh/ssh-edit.html',ssh=ssh)

@ssh.route('/edit',methods = ['POST','GET'])
def edit():
    id = request.form['id']
    ssh = Ssh.query.get(id)
    ssh.name = request.form['name']
    ssh.username = request.form['username']
    ssh.password = request.form['password']
    ssh.ip = request.form['ip']
    ssh.port = request.form['port']
    ssh.updated_at = datetime.now()

    db.session.commit()

    return redirect('list')

@ssh.route('/delete',methods = ['GET'])
def delete():
    id = request.args.get("id")
    ssh = Ssh.query.get(id)
    ssh.deleted_at = datetime.now()

    db.session.commit()

    return redirect('list')

'''
@ssh.route('/to_detail',methods = ['POST','GET'])
def to_detail():
    id = request.args.get("id")
    ssh = ssh.query.filter_by(id=id).first()
    roles = Role.query.filter(Role.state == 1)
    return render_template('ssh/ssh-detail.html',ssh=ssh,roles=roles)




'''