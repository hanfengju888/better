from flask import Flask,render_template,request,session,redirect,url_for,Blueprint
from flask import render_template
from datetime import datetime

from app.models import db
from app.models.role import Role
from app.models.user import User

user = Blueprint("user",__name__,url_prefix='/user')

#进入用户管理列表页
@user.route('/list',methods = ['POST','GET'])
def to_list():
    sign = request.args.get('sign')
    if sign is not None:
        session['sign'] = sign

    users = User.query.filter(User.deleted_at == None)
    roles = Role.query.filter(Role.state == 1)

    return render_template('user/user.html',users=users,roles=roles)

@user.route('/to_add',methods = ['GET'])
def to_add():
    roles = Role.query.filter(Role.state == 1)

    return render_template('user/user-add.html',roles=roles)

@user.route('/add',methods = ['POST'])
def add():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    role = request.form['role']


    #插入数据
    wait_add_user = User(name=name,username=username,password=password,email=email,role=role)
    db.session.add(wait_add_user)
    db.session.commit()

    return redirect('list')


@user.route('/to_edit',methods = ['POST','GET'])
def to_edit():
    id = request.args.get("id")
    user = User.query.filter_by(id=id).first()
    roles = Role.query.filter(Role.state == 1)
    return render_template('user/user-edit.html',user=user,roles=roles)

@user.route('/edit',methods = ['POST','GET'])
def edit():
    id = request.form['id']
    user = User.query.get(id)
    user.name = request.form['name']
    user.username = request.form['username']
    user.password = request.form['password']
    user.email = request.form['email']
    user.role = request.form['role']
    user.updated_at = datetime.now()

    db.session.commit()

    return redirect('list')

@user.route('/to_detail',methods = ['POST','GET'])
def to_detail():
    id = request.args.get("id")
    user = User.query.filter_by(id=id).first()
    roles = Role.query.filter(Role.state == 1)
    return render_template('user/user-detail.html',user=user,roles=roles)


@user.route('/delete',methods = ['GET'])
def delete():
    id = request.args.get("id")
    user = User.query.get(id)
    user.deleted_at = datetime.now()

    db.session.commit()

    return redirect('list')