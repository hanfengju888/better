import datetime

from flask import Flask, render_template, request, session, redirect, url_for, Blueprint, jsonify
from app.utils.executor import Executor
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

#添加用例时
@case.route("/send_http",methods=["POST"])
@permission()
def send_http(user_info):
    #flag 标记是点击的请求按钮 0   还是保存按钮 1
    flag = request.form["flag"]
    method = request.form["request_method"]
    url = request.form["url"]
    payload = request.form["payload"]
    project_id = request.form["project_id"]
    project = Project.query.get(project_id)
    headers = {'accessToken': project.accessToken,'requestType':'1'}

    if flag == "0":
        if payload is not None and payload != "":
            payload = payload.replace("'", '"')
            json_payload = json.loads(payload)
            # 上传资源特殊处理
            if json_payload.get('modeFile') is not None:
                file_path = json_payload.get('modeFile')
                files = [('modeFile', (file_path.split("/")[-1], open(file_path, 'rb'), 'text/csv'))]
                del json_payload['modeFile']
                r = Request(url, data=json_payload, headers=headers, files=files, verify=False)
                response = r.request(method)
            else:
                r = Request(url, data=payload, headers=headers)
                response = r.request(method)
        else:
            r = Request(url, data=payload, headers=headers)
            response = r.request(method)

        if not response.get("status"):
            return jsonify(dict(code=110, data=response, msg=response.get("msg")))



        return render_template('case/case-add.html', method=method,project=project,url=url,payload=payload,response=json.dumps(response,sort_keys=True,indent=2,ensure_ascii=False))
    else:
        #保存到数据库
        expected = request.form["expected"]
        name = request.form.get("name")
        test_case =  TestCase(name, 1, url, project_id, "", payload,1, expected, user_info.get("id") ,request_method=method)
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

#执行用例
@case.route("/execute",methods=['GET','POST'])
def execute_case():
    id_list = request.args.get("id_list")
    print(id_list)
    for id in id_list.split(","):
        result,err = Executor.run(id)
        if err is None:
            print(result)
        else:
            print(err)


@case.route('/to_edit',methods = ['POST','GET'])
def case_to_edit():
    id = request.args.get("id")
    project_id = request.args.get("project_id")
    case = TestCase.query.filter_by(id=id).first()
    if case.body is not None and case.body != "":
        case.body = json.dumps(json.loads(case.body),indent=2,ensure_ascii=False)
    project = Project.query.filter_by(id=project_id).first()
    assert_dic = dict(expected=case.expected,acutal='',assert_result='')
    return render_template('case/case-edit.html',case=case,project=project,assert_dic=assert_dic)


@case.route('/send_http_edit',methods = ['POST','GET'])
def case_edit():
    # flag 标记是点击的请求按钮 0   还是保存按钮 1
    id = request.form["case_id"]
    flag = request.form["flag"]
    method = request.form["request_method"]
    url = request.form["url"]
    payload = request.form["payload"]
    #gest
    project_id = request.form["project_id"]
    project = Project.query.get(project_id)
    headers = {'accessToken': project.accessToken,'requestType':'1'}
    if flag == "0":
        if len(payload) > 3:
            payload = payload.replace("'", '"')
            json_payload = json.loads(payload)
            # 上传资源特殊处理
            if json_payload.get('modeFile') is not None:
                file_path = json_payload.get('modeFile')
                files = [('modeFile', (file_path.split("/")[-1], open(file_path, 'rb'), 'text/csv'))]
                del json_payload['modeFile']
                r = Request(url, data=json_payload, headers=headers, files=files, verify=False)
                response = r.request(method)
            else:
                headers['Content-Type'] = 'application/json'
                r = Request(url, data=payload, headers=headers)
                response = r.request(method)
        else:
            headers['Content-Type'] = 'application/json'
            r = Request(url, data=payload, headers=headers)
            response = r.request(method)

        if not response.get("status"):
            return jsonify(dict(code=110, data=response, msg=response.get("msg")))

        case = TestCase.query.filter_by(id=id).first()
        if len(case.body) > 3:
            case.body = json.dumps(json.loads(case.body), indent=2, ensure_ascii=False)

        assert_dic = {}
        assert_dic['expected'] = case.expected
        print(response)
        assert_dic['actual'] = response['response']['code']
        assert_result = assert_dic.get("expected") == assert_dic.get('actual')
        assert_result = '成功' if assert_result else '失败'
        assert_dic['assert_result'] = assert_result

        return render_template('case/case-edit.html', assert_dic=assert_dic,project=project, case=case,response=json.dumps(response,sort_keys=True,indent=2,ensure_ascii=False))
    else:
        # 保存到数据库
        test_case = TestCase.query.get(id)
        test_case.name = request.form.get("name")
        test_case.request_method = method
        test_case.url = url
        test_case.body = payload
        test_case.updated_at = datetime.datetime.now()
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


# @case.route('/case/to_detail',methods = ['POST','GET'])
# def case_to_detail():
#     id = request.args.get("id")
#     case = Case.query.filter_by(id=id).first()
#
#     return render_template('case/case-detail.html',case=case)
#
#
