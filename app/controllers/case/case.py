import datetime

from flask import Flask, render_template, request, session, redirect, url_for, Blueprint, jsonify

import json

from app.middleware.HttpClient import Request
from app.models import db
from app.models.project import Project
from app.models.test_case import TestCase
from app.utils.SingletonDecorator import permission

case = Blueprint("case",__name__,url_prefix='/case')

@case.route('/to_add',methods = ['GET'])
def case_to_add():
    project_id = request.args.get('project_id')
    project = Project.query.get(project_id)

    return render_template('case/case-add.html',project=project)

@case.route("/send_http",methods=["POST"])
@permission()
def send_http(user_info):
    #flag 标记是点击的请求按钮 0   还是保存按钮 1
    flag = request.form["flag"]
    method = request.form["request_method"]
    url = request.form["url"]
    payload = request.form["payload"]
    headers = None
    project_id = request.form["project_id"]
    project = Project.query.get(project_id)

    if flag == "0":
        r = Request(url, data=payload, headers=headers)
        response = r.request(method)

        if not response.get("status"):
            return jsonify(dict(code=110, data=response, msg=response.get("msg")))



        return render_template('case/case-add.html', project=project,url=url,payload=payload,response=response)
    else:
        #保存到数据库
        test_case =  TestCase('1', 1, url, project_id, "", payload,1, "expected", user_info.get("id") )
        db.session.add(test_case)
        db.session.commit()
        return redirect(f"/project/to_detail_with_param/{project_id}")

# 删除用例
@case.route('/delete',methods = ['GET'])
def case_delete():
    case_id = request.args.get("case_id")
    project_id = request.args.get("project_id")
    case = TestCase.query.get(case_id)
    case.deleted_at = datetime.datetime.now()
    db.session.commit()

    return redirect(f"/project/to_detail_with_param/{project_id}")

#
# @case.route('/case/add',methods = ['POST'])
# def case_add():
#     module_id = request.form['module_id']
#     module_name = request.form['module_name']
#     case_name = request.form['case_name']
#     case_detail = request.form['case_detail']
#     expect_type = request.form['expect_type']
#     expect_result = request.form['expect_result']
#     remark = request.form['remark']
#
#     #插入数据
#     wait_add_case = Case(create_time=utils.get_now_time(),module_id=module_id,module_name=module_name,case_detail=case_detail,case_name=case_name,expect_type=expect_type,expect_result=expect_result,remark=remark,state="1")
#     DB.session.add(wait_add_case)
#     DB.session.commit()
#
#     #更新下module中的case_count
#
#     cases = Case.query.filter(Case.state == '1', Case.module_id == module_id)
#     module = Module.query.filter_by(id=module_id).first()
#     module.case_count = cases.count()
#     DB.session.commit()
#
#     cases = Case.query.filter(Case.state == '1', Case.module_id == module_id)
#
#     return render_template('case/case.html', cases=cases, module=module)
#
#
#
# @case.route('/case/to_edit',methods = ['POST','GET'])
# def case_to_edit():
#     id = request.args.get("id")
#     case = Case.query.filter_by(id=id).first()
#
#     return render_template('case/case-edit.html',case=case)
#
# @case.route('/case/edit',methods = ['POST','GET'])
# def case_edit():
#     id = request.form['id']
#     case = Case.query.get(id)
#     case.case_name = request.form['case_name']
#     case.case_detail = request.form['case_detail']
#     case.expect_type = request.form['expect_type']
#     case.expect_result = request.form['expect_result']
#     case.remark = request.form['remark']
#     case.update_time = utils.get_now_time()
#
#     DB.session.commit()
#
#     module = Module.query.filter_by(id=case.module_id).first()
#     cases = Case.query.filter(Case.state == '1', Case.module_id == case.module_id)
#
#     return render_template('case/case.html', cases=cases, module=module)
#
# @case.route('/case/to_detail',methods = ['POST','GET'])
# def case_to_detail():
#     id = request.args.get("id")
#     case = Case.query.filter_by(id=id).first()
#
#     return render_template('case/case-detail.html',case=case)
#
#
