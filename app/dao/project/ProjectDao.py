from sqlalchemy import or_

from app import better
from app.dao.project.ProjectRoleDao import ProjectRoleDao
from app.models import db
from app.models.project import Project
from app.utils.logger import Log


class ProjectDao(object):
    log = Log("ProjectDao")

    @staticmethod
    def list_project(user_id,role,page,size,name=None):
        """查询/获取项目列表"""
        try:
            search = [Project.deleted_at == None]
            if role != better.config.get("ADMIN"):
                project_list,err = ProjectRoleDao.list_project_by_user(user_id)
                search.append(or_(Project.id in project_list,Project.owner==user_id,Project.private==0))

            if name:
                search.append(Project.name.ilike(f"%{name}%"))
            data = Project.query.filter(*search)
            total = data.count()
            return data.order_by(Project.created_at.desc()).paginate(page,per_page=size).items,total,None
        except Exception as e:
            ProjectDao.log.error(f"获取用户:{user_id}项目列表失败,{e}")
            return [],0,f"获取用户：{user_id}项目列表失败,{e}"

    @staticmethod
    def add_project(name,owner,user,private,description=""):
        try:
            data = Project.query.filter_by(name=name,deleted_at=None).first()
            if data is not None:
                return "项目已存在"
            pr = Project(name,owner,user,private,description)
            db.session.add(pr)
            db.session.commit()
        except Exception as e:
            ProjectDao.log.error(f"新增项目:{name}失败，{e}")
            return 0,0,f"新增项目:{name}失败,{e}"