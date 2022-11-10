from app.models import db
from app.models.user import User
from app.models.project import Project
from app.models.project_role import ProjectRole
from app.models.test_case import TestCase
from app.models.role import Role
from app.models.database import Database

db.create_all()