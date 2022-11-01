from flask import Blueprint, request, jsonify, session,render_template

from app import better
from app.dao.project.ProjectDao import ProjectDao
from app.handler.factory import ResponseFactory
from app.handler.page import PageHandler
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
        return render_template("project/project.html",data=ResponseFactory.model_to_dict(result))
    return jsonify(dict(code=0,data=ResponseFactory.model_to_dict(result),msg="操作成功"))

@pr.route("/insert",methods=["POST"])
@permission(role="MANAGER")
def insert_project(user_info):
    try:
        user_id = user_info["id"]
        data = request.get_json()
        if not data.get("name") or not data.get("owner"):
            return jsonify(dict(code=101,msg="项目名称/项目负责人不能为空"))
        private = data.get("private",0)
        err = ProjectDao.add_project(data.get("name"),data.get("owner"),user_id,private)
        if err is not None:
            return jsonify(dict(code=110,msg=err))
        return jsonify(dict(code=0, msg="操作成功"))
    except Exception as e:
        return jsonify(dict(code=111,msg=str(e)))
