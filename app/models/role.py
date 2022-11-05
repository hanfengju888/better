from app.models import db
from datetime import datetime

class Role(db.Model):
    # 定义表名
    __tablename__ = "role"
    # 重新定义现有对象和列
    __table_args__ = {'extend_existing': True}
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_code = db.Column(db.String(64), comment="角色编码")
    role_name = db.Column(db.String(64), comment="角色名称")
    remark = db.Column(db.String(64), comment="备注")
    state = db.Column(db.INT, comment="1正常,0删除")

    def __init__(self, role_code, role_name, remark,state=1):
        self.role_code = role_code
        self.role_name = role_name
        self.remark = remark
        self.state = state