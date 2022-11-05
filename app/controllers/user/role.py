from flask import Flask,render_template,request,session,redirect,Blueprint

from app.models import db
from app.models.role import Role

role = Blueprint("role",__name__,url_prefix='/role')

#角色管理
#进入用户管理列表页
@role.route('/list',methods = ['POST','GET'])
def role_to_list():
    sign = request.args.get('sign')
    if sign is not None:
        session['sign'] = sign

    roles = Role.query.filter(Role.state=='1')

    return render_template('role/role.html',roles=roles)

@role.route('/to_add',methods = ['GET'])
def role_to_add():

    return render_template('role/role-add.html')

@role.route('/add',methods = ['POST'])
def role_add():
    role_code = request.form['role_code']
    role_name = request.form['role_name']
    remark = request.form['remark']

    #插入数据
    wait_add_role = Role(role_code=role_code,role_name=role_name,remark=remark)
    db.session.add(wait_add_role)
    db.session.commit()

    return redirect('list')


@role.route('/to_edit',methods = ['POST','GET'])
def role_to_edit():
    id = request.args.get("id")
    role = Role.query.filter_by(id=id).first()
    return render_template('role/role-edit.html',role=role)

@role.route('/edit',methods = ['POST','GET'])
def role_edit():
    id = request.form['id']
    role = Role.query.get(id)
    role.role_code = request.form['role_code']
    role.role_name = request.form['role_name']
    role.remark = request.form['remark']

    db.session.commit()

    return redirect('list')


@role.route('/delete',methods = ['GET'])
def role_delete():
    id = request.args.get("id")
    role = Role.query.get(id)
    role.state = 0

    db.session.commit()

    return redirect('list')