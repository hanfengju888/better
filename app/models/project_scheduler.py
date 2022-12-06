from app.models import db
from datetime import datetime
import time

class ProjectScheduler(db.Model):
    id = db.Column(db.INT,primary_key=True)
    project_id = db.Column(db.INT)
    project_name = db.Column(db.String(160))
    user_id = db.Column(db.INT)
    username = db.Column(db.String(160))
    name = db.Column(db.String(160))
    execute_count = db.Column(db.INT)
    ps_id = db.Column(db.String(32),comment="创建job时使用的id")
    trigger = db.Column(db.String(64), comment="触发器类型: date,interval,cron")
    rule = db.Column(db.String(64),comment="秒—分-时-日-月-星期")
    created_at = db.Column(db.DATETIME, nullable=False)
    updated_at = db.Column(db.DATETIME, nullable=False)
    deleted_at = db.Column(db.DATETIME)
    status = db.Column(db.String(64),comment="0:被删除 1：运行中  2：暂停中")

    def __init__(self, project_id, project_name,name, user_id,username,trigger,rule):
        self.project_id = project_id
        self.project_name = project_name
        self.user_id = user_id
        self.username = username
        self.ps_id = 'scheduler_' + str(time.strftime('%Y%m%d%H%M%S'))
        self.name = name
        self.trigger = trigger
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.rule = rule
        self.status = '1'
        self.execute_count = 0

    def __repr__(self):
        return '<ProjectScheduler %r>' % self.name