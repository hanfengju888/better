import json
import re
from datetime import datetime

from flask import render_template
from flask import request, session, redirect, Blueprint

from app.models import db
from app.models.mock import Mock
from app.utils.logger import Log

mock = Blueprint("mock",__name__,url_prefix='/mock')

log = Log("mock")



#mock测试
@mock.route('/<string:path>',methods=['POST','GET'])
def mockk(path,id=0):
    method = request.method
    path = '/' + path
    header = request.headers.get('Content-Type')
    if method == "POST":
        json_body = request.get_json()
        sorted_json_body = dict(sorted(json_body.items(),key=lambda x:x[0] ))
        body = json.dumps(sorted_json_body)
        body = re.sub(r' |\r|\n|\t','',body)
        mock = Mock.query.filter_by(path=path,header=header,body=body,deleted_at=None,status='1').first()
        if mock is not None:
            mock.use_count += 1
            db.session.commit()
            return mock.response_data
    elif method =="GET":
        json_args = dict(request.args)
        final_path = f'{path}?'
        for k,v in json_args.items():
            final_path += f'{k}={v}'

        mock = Mock.query.filter_by(path=final_path,deleted_at=None,status='1').first()
        if mock is not None:
            mock.use_count += 1
            db.session.commit()
            return mock.response_data

    return {'code':0,'data':'未找到记录'}

#进入列表页
@mock.route('/list',methods = ['POST','GET'])
def to_list():
    sign = request.args.get('sign')
    if sign is not None:
        session['sign'] = sign

    mocks = Mock.query.filter(Mock.deleted_at == None)


    return render_template('mock/mock.html',mocks=mocks)


@mock.route('/to_add',methods = ['GET'])
def to_add():

    return render_template('mock/mock-add.html')

@mock.route('/add',methods = ['POST'])
def add():
    method = request.form.get('method')
    name = request.form.get('name')
    path = request.form.get('path')
    header = request.form.get('header')
    body = request.form.get('body')
    response_data = request.form.get('response_data')

    if method == "GET":
        header = ''

    if body is not None and body != '':
        json_body = json.loads(body)
        sorted_json_body = dict(sorted(json_body.items(), key=lambda x: x[0]))
        body = json.dumps(sorted_json_body)
        body = re.sub(r' |\r|\n|\t','',body)

        if response_data is None or response_data == "":
            json_esponse_data = {'code':200,'data':sorted_json_body}
            response_data = json.dumps(json_esponse_data,indent=4,ensure_ascii=False)

    #插入数据
    wait_Mock = Mock(name,path,method,header,body,response_data)
    db.session.add(wait_Mock)
    db.session.commit()

    return redirect('list')


@mock.route('/to_edit',methods = ['POST','GET'])
def to_edit():
    id = request.args.get("id")
    mock = Mock.query.filter_by(id=id).first()
    if mock.body is not None and mock.body != "":
        mock.body = json.dumps(json.loads(mock.body),indent=4,ensure_ascii=False)
    return render_template('mock/mock-edit.html',mock=mock)


@mock.route('/edit',methods = ['POST','GET'])
def edit():
    id = request.form['id']

    method = request.form.get('method')
    name = request.form.get('name')
    path = request.form.get('path')
    header = request.form.get('header')
    body = request.form.get('body')
    response_data = request.form.get('response_data')



    mock = Mock.query.get(id)
    mock.method = method
    mock.name = name
    mock.path = path
    mock.header = header

    if method == "GET":
        mock.header = ''

    if  body is not None and body != '':
        json_body = json.loads(body)
        sorted_json_body = dict(sorted(json_body.items(),key=lambda x:x[0]))
        body = json.dumps(sorted_json_body)
        mock.body  = re.sub(r' |\r|\n|\t', '', body)

        #如果不填写返回结果，则返回{'code':200,'data':body}
        if response_data is None or response_data == "":
            json_esponse_data = {'code':200,'data':sorted_json_body}
            response_data = json.dumps(json_esponse_data,indent=4,ensure_ascii=False)

    mock.response_data = response_data
    mock.updated_at = datetime.now()

    db.session.commit()

    return redirect('list')


@mock.route('/delete',methods = ['GET'])
def delete():
    id = request.args.get("id")
    mock = Mock.query.get(id)
    mock.deleted_at = datetime.now()

    db.session.commit()

    return redirect('list')

@mock.route('/change_status',methods = ['POST','GET'])
def change_status():
    id = request.args.get("id")
    status = request.args.get("status")
    mock = Mock.query.filter_by(id=id).first()
    mock.status = status
    db.session.commit()
    return redirect('list')




