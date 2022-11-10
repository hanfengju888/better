import copy

from flask import Flask,render_template,request,session,redirect,url_for,Blueprint
from flask import render_template
from datetime import datetime

from app.models import db
from app.models.role import Role
from app.models.user import User
from app.models.database import Database
from app.utils.SingletonDecorator import permission
from app.utils.DataBaseUtil import DatabaseUtil
from app.utils.logger import Log

database = Blueprint("database",__name__,url_prefix='/database')
log = Log("dataBase")

#进入数据库管理列表页
@database.route('/list',methods = ['POST','GET'])
def to_list():
    sign = request.args.get('sign')
    if sign is not None:
        session['sign'] = sign

    databases = Database.query.filter(Database.deleted_at == None)

    return render_template('database/database.html',databases=databases)

@database.route('/to_add',methods = ['GET'])
def to_add():

    return render_template('database/database-add.html')

@database.route('/add',methods = ['POST'])
@permission()
def add(user_info):
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    sql_type = request.form['sql_type']
    host = request.form['host']
    port = request.form['port']
    database_name = request.form['database_name']
    create_user = user_info.get("id")
    connect_status = "success"
    try:
        DatabaseUtil(host, user=username, password=password, database=database_name, port=port)
    except Exception as e:
        log.error(f"连接数据库{host}失败: {str(e)}")
        connect_status = str(e)

    #插入数据
    wait_add_database = Database(name=name,host=host,port=port,username=username,password=password,database_name=database_name,create_user=create_user,sql_type=sql_type,connect_status=connect_status)
    db.session.add(wait_add_database)
    db.session.commit()

    return redirect('list')


@database.route('/to_edit',methods = ['POST','GET'])
def to_edit():
    id = request.args.get("id")
    database = Database.query.filter_by(id=id).first()

    return render_template('database/database-edit.html',database=database,)

@database.route('/edit',methods = ['POST','GET'])
def edit():
    id = request.form['id']
    database = Database.query.get(id)
    database.sername = request.form['username']
    database.name = request.form['name']
    database.password = request.form['password']
    database.sql_type = request.form['sql_type']
    database.host = request.form['host']
    database.port = request.form['port']
    database.database_name = request.form['database_name']
    database.connect_status = "success"
    try:
        DatabaseUtil(database.host, user=database.username, password=database.password, database=database.database_name, port=database.port)
    except Exception as e:
        log.error(f"连接数据库{database.host}失败: {str(e)}")
        database.connect_status = str(e)
    db.session.commit()



    return redirect('list')

@database.route('/to_detail',methods = ['POST','GET'])
def to_detail():
    id = request.args.get("id")
    user = Database.query.filter_by(id=id).first()
    roles = Role.query.filter(Role.state == 1)
    return render_template('database/user-detail.html',user=user,roles=roles)


@database.route('/delete',methods = ['GET'])
def delete():
    id = request.args.get("id")
    database = Database.query.get(id)
    database.deleted_at = datetime.now()

    db.session.commit()

    return redirect('list')

#执行SQL
@database.route('/to_execute',methods = ['POST','GET'])
def to_execute():
    id = request.args.get("id")
    database = Database.query.filter_by(id=id).first()

    table_cursor = DatabaseUtil(database.host, user=database.username, password=database.password, database=database.database_name,
                 port=database.port)
    desc_cursor = DatabaseUtil(database.host, user=database.username, password=database.password,
                                database=database.database_name,
                                port=database.port)

    sql = "show tables;"
    # sql = "select * from user"
    result_list = table_cursor.execute_sql(table_cursor.cursor,sql)
    return_list = []
    first_number = 1
    print(result_list)
    for v in result_list:
        second_number = 0
        table_name = v[0]
        sql = f"desc `{table_name}`;"
        return_list.append([first_number,second_number,table_name])
        second_number = first_number
        first_number += 1

        desc_list = desc_cursor.execute_sql(desc_cursor.cursor, sql)
        for m in desc_list:
            return_list.append([first_number,second_number,m[0] +" "+m[1]])
            first_number += 1

    return render_template('database/database-execute.html',database=database,result_list=result_list,return_list=return_list)