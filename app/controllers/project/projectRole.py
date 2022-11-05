import datetime

from flask import Blueprint, request, jsonify, session,render_template,redirect

from app import better
from app.dao.project.ProjectDao import ProjectDao
from app.dao.project.ProjectRoleDao import ProjectRoleDao
from app.handler.factory import ResponseFactory
from app.handler.page import PageHandler
from app.models import db
from app.models.project import Project
from app.models.project_role import ProjectRole
from app.models.role import Role
from app.models.user import User
from app.utils.SingletonDecorator import permission

projectRole = Blueprint("projectRole", __name__, url_prefix="/projectRole")


@projectRole.route("/delete",methods=["GET"])
@permission()
def delete(user_info):
    project_role_id = request.args.get("project_role_id")
    p = ProjectRole.query.get(project_role_id)
    p.deleted_at = datetime.datetime.now()
    db.session.commit()

    id = request.args.get("project_id")
    project = Project.query.filter_by(id=id).first()
    user_objects = User.query.all()

    #成员管理tab页
    #项目绑定的用户
    user_list, project_role_id = ProjectRoleDao.list_user_by_project_id(id)
    #角色信息
    roles = Role.query.filter(Role.state == 1)
    return render_template("project/project-edit.html",roles=roles,project_role_id=project_role_id,user_list=ResponseFactory.model_to_dict(user_list),project=project,data=ResponseFactory.model_to_dict(user_objects))




