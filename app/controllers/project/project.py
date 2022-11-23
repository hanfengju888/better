from flask import Blueprint, request, jsonify, session,render_template,redirect

from app import better
from app.dao.project.ProjectDao import ProjectDao
from app.dao.project.ProjectRoleDao import ProjectRoleDao
from app.handler.factory import ResponseFactory
from app.handler.page import PageHandler
from app.models.project import Project
from app.models.role import Role
from app.models.test_case import TestCase
from app.models.user import User
from app.utils.SingletonDecorator import permission

pr = Blueprint("project", __name__, url_prefix="/project")


@pr.route("/list")
@permission()
def list_project(user_info):
    """
    获取项目列表
    :param user_info:
    :return:
    """

    sign = request.args.get("sign")
    if sign is not None:
        session["sign"] = sign


    page,size = PageHandler.page()
    user_role,user_id = user_info["role"],user_info["id"]
    name = request.args.get("name")
    result,total,err = ProjectDao.list_project(user_id,user_role,page,size,name)
    if err is not None:
        return jsonify(dict(code=110,data=result,msg=err))
    if not result:
        return jsonify(dict(code=0,data=[],msg="操作成功"))

    if sign is not None:
        return render_template("project/project.html",data=ResponseFactory.model_to_dict(result),total=total)
    return jsonify(dict(code=0,data=ResponseFactory.model_to_dict(result),msg="操作成功"))


@pr.route("/list_ui")
@permission()
def list_project_ui(user_info):
    """
    获取项目列表
    :param user_info:
    :return:
    """
    #标记页面左侧菜单
    sign = request.args.get("sign")
    if sign is not None:
        session["sign"] = sign


    page, size = PageHandler.page()
    user_role, user_id = user_info["role"], user_info["id"]
    name = request.args.get("name")
    result, total, err = ProjectDao.list_project(user_id, user_role, page, size, name)
    max_page = int(total/size + 1)

    return render_template("project/project.html", data=ResponseFactory.model_to_dict(result),name=name,total=total,max_page=max_page,page=page)

@pr.route("/insert",methods=["POST"])
@permission(role="MANAGER")
def insert_project(user_info):

    data = request.get_json()
    #走接口
    if data is not None:
        try:
            user_id = user_info["id"]

            if not data.get("name") or not data.get("owner"):
                return jsonify(dict(code=101,msg="项目名称/项目负责人不能为空"))
            private = data.get("private",0)
            err = ProjectDao.add_project(data.get("name"),data.get("owner"),user_id,private)
            if err is not None:
                return jsonify(dict(code=110,msg=err))
            return jsonify(dict(code=0, msg="操作成功"))
        except Exception as e:
            return jsonify(dict(code=111,msg=str(e)))
    #走页面
    else:
        name = request.form["name"]
        owner = int(request.form["owner"])
        description = request.form["description"]
        private = int(request.form["private"])
        print(private)
        err = ProjectDao.add_project(name, owner, owner, private,description)
        if err is None:
            return redirect("list_ui")
        print(err)


@pr.route("/to_insert",methods=["GET"])
@permission()
def to_insert(user_info):
    user_objects = User.query.all()
    return render_template("project/project-add.html",data=ResponseFactory.model_to_dict(user_objects))

#查看项目详情--页面过来的
@pr.route("/to_detail",methods=["GET"])
@permission()
def to_detail(user_info):
    id = request.args.get("id")
    project = Project.query.filter_by(id=id).first()
    user_objects = User.query.all()

    #成员管理tab页
    #项目绑定的用户

    user_list, project_role_id = ProjectRoleDao.list_user_by_project_id(id)
    #角色信息
    roles = Role.query.filter(Role.state == 1)

    #用例信息
    testcases = TestCase.query.filter_by(project_id=id,deleted_at=None).all()

    return render_template("project/project-edit.html",cases=testcases,roles=roles,project_role_id=project_role_id,user_list=ResponseFactory.model_to_dict(user_list),project=project,data=ResponseFactory.model_to_dict(user_objects))


#查看项目详情--带参数，其他方法redirect过来的
@pr.route("/to_detail_with_param/<int:id>",methods=["GET"])
def to_detail_with_param(id):
    project = Project.query.filter_by(id=id).first()
    user_objects = User.query.all()

    #成员管理tab页
    #项目绑定的用户

    user_list, project_role_id = ProjectRoleDao.list_user_by_project_id(id)
    #角色信息
    roles = Role.query.filter(Role.state == 1)

    #用例信息
    testcases = TestCase.query.filter_by(project_id=id,deleted_at=None).all()

    return render_template("project/project-edit.html",cases=testcases,roles=roles,project_role_id=project_role_id,user_list=ResponseFactory.model_to_dict(user_list),project=project,data=ResponseFactory.model_to_dict(user_objects))


#更新项目
@pr.route("/update",methods=["POST"])
@permission()
def update(user_info):
    id = request.form["id"]
    name = request.form["name"]
    accessToken = request.form["accessToken"]
    owner = int(request.form["owner"])
    description = request.form["description"]
    private = int(request.form["private"])
    ProjectDao.add_project(name, owner, owner, private,description,id,accessToken)

    return redirect("list_ui")




