from app.models import db
from app.models.project_role import ProjectRole
from app.models.user import User
from app.utils.logger import Log

class ProjectRoleDao(object):
    log = Log("ProjectRoleDao")

    @staticmethod
    def list_project_by_user(user_id):
        """
        通过user_id获取项目列表
        :param user_id:
        :return:
        """
        try:
            projects = ProjectRole.query.filter_by(user_id=user_id,deleted_at=None).all()
            return [p.id for p in projects],None
        except Exception as e:
            ProjectRoleDao.log.error(f"查询用户:{user_id}项目失败,{e}")
            return [],f"查询项目失败,{e}"

    @staticmethod
    def add_project_role(user_id,project_id,project_role,user):
        try:
            role = ProjectRole.query.filter_by(user_id=user_id,project_id=project_id,project_role=project_role,deleted_at=None).first()
            if role is not None:
                return "该用户已存在"
            role = ProjectRole(user_id,project_id,project_role,user)
            db.session.add(role)
            db.session.commit()
        except Exception as e:
            ProjectRoleDao.log.error(f"添加项目用户失败,{e}")
            return f"添加项目用户失败,{e}"

        return None

    @staticmethod
    def list_user_by_project_id(project_id):
        """

        :param project_id: 通过Project_id获取user
        :return:
        """

        try:
            project_roles = ProjectRole.query.filter_by(project_id=project_id,deleted_at=None).all()
            project_role_id = None
            if len(project_roles) > 0:
                project_role_id = project_roles[0].id
            return [User.query.filter_by(id=p.user_id).first() for p in project_roles],project_role_id
        except Exception as e:
            ProjectRoleDao.log.error(f"查询项目:{project_id}用户失败,{e}")
            return [],f"查询用户失败,{e}"