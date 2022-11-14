import copy

from flask import Flask,render_template,request,session,redirect,url_for,Blueprint
from flask import render_template
from datetime import datetime
import redis
from app.models import db
from app.models.redis import Redis
from app.utils.SingletonDecorator import permission
from app.utils.logger import Log

rediss = Blueprint("rediss",__name__,url_prefix='/redis')
log = Log("rediss")

#进入redis管理列表页
@rediss.route('/list',methods = ['POST','GET'])
def to_list():
    sign = request.args.get('sign')
    if sign is not None:
        session['sign'] = sign

    redises = Redis.query.filter(Redis.deleted_at == None)

    return render_template('redis/redis.html',redises=redises)

@rediss.route('/to_add',methods = ['GET'])
def to_add():

    return render_template('redis/redis-add.html')

@rediss.route('/add',methods = ['POST'])
@permission()
def add(user_info):
    name = request.form['name']
    password = request.form['password']
    host = request.form['host']
    port = request.form['port']
    db_number = request.form['db_number']
    redis_key_count = 0
    try:
        r = redis.Redis(host, password=password, port=port, decode_responses=True)
        redis_key_count = len(r.keys())
    except Exception as e:
        log.error(f"连接redis数据库{host}失败: {str(e)}")

    #插入数据
    wait_add_redis = Redis( env=0,name=name,addr='',host=host,port=port,password=password,db_number=db_number , cluster=0,key_count=redis_key_count)
    db.session.add(wait_add_redis)
    db.session.commit()

    return redirect('list')

@rediss.route('/delete',methods = ['GET'])
def delete():
    id = request.args.get("id")
    redis = Redis.query.get(id)
    redis.deleted_at = datetime.now()

    db.session.commit()

    return redirect('list')

@rediss.route('/to_edit',methods = ['POST','GET'])
def to_edit():
    id = request.args.get("id")
    redis = Redis.query.filter_by(id=id).first()

    return render_template('redis/redis-edit.html',redis=redis,)

@rediss.route('/edit',methods = ['POST','GET'])
def edit():
    id = request.form['id']
    redi = Redis.query.get(id)
    redi.name = request.form['name']
    redi.password = request.form['password']
    redi.host = request.form['host']
    redi.port = request.form['port']
    redi.db_number = request.form['db_number']

    try:
        r = redis.Redis(host=redi.host, password=redi.password, port=redi.port, decode_responses=True)
        redi.key_count = len(r.keys())
    except Exception as e:
        log.error(f"连接数据库{redi.host}失败: {str(e)}")

    redi.updated_at = datetime.now()
    db.session.commit()

    return redirect('list')


'''


@redis.route('/to_detail',methods = ['POST','GET'])
def to_detail():
    id = request.args.get("id")
    user = redis.query.filter_by(id=id).first()
    roles = Role.query.filter(Role.state == 1)
    return render_template('redis/user-detail.html',user=user,roles=roles)




#执行SQL
@redis.route('/to_execute',methods = ['POST','GET'])
def to_execute():
    id = request.args.get("id")
    redis = redis.query.filter_by(id=id).first()

    table_cursor = redisUtil(redis.host, user=redis.username, password=redis.password, redis=redis.redis_name,
                 port=redis.port)
    desc_cursor = redisUtil(redis.host, user=redis.username, password=redis.password,
                                redis=redis.redis_name,
                                port=redis.port)

    sql = "show tables;"
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

    return render_template('redis/redis-execute.html',redis=redis,result_list=result_list,return_list=return_list)


#执行SQL
@redis.route('/execute_sql',methods = ['POST','GET'])
def execute_sql():
    execute_sql = request.args.get("sql")
    id = request.args.get("redis_id")
    redis = redis.query.filter_by(id=id).first()
    cursor = redisUtil(redis.host, user=redis.username, password=redis.password,
                                redis=redis.redis_name,
                                port=redis.port)
    table_name = execute_sql.split(" ")[-1]
    title_list = cursor.execute_sql(cursor.cursor,f"desc `{table_name}`")
    final_title_list = []
    for i in title_list:
        final_title_list.append(i[0])

    value_list = cursor.execute_sql(cursor.cursor,execute_sql)

    table_cursor = redisUtil(redis.host, user=redis.username, password=redis.password,
                                redis=redis.redis_name,
                                port=redis.port)
    desc_cursor = redisUtil(redis.host, user=redis.username, password=redis.password,
                               redis=redis.redis_name,
                               port=redis.port)

    sql = "show tables;"
    result_list = table_cursor.execute_sql(table_cursor.cursor, sql)
    return_list = []
    first_number = 1
    for v in result_list:
        second_number = 0
        table_name = v[0]
        sql = f"desc `{table_name}`;"
        return_list.append([first_number, second_number, table_name])
        second_number = first_number
        first_number += 1

        desc_list = desc_cursor.execute_sql(desc_cursor.cursor, sql)
        for m in desc_list:
            return_list.append([first_number, second_number, m[0] + " " + m[1]])
            first_number += 1

    return render_template('redis/redis-execute.html',redis=redis,sql=execute_sql,value_list=value_list,title_list=final_title_list,result_list=result_list,return_list=return_list)
'''