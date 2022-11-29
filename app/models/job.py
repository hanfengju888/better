from app.models import db
from datetime import datetime

class Job(db.Model):
    id = db.Column(db.INT,primary_key=True)
    project_id = db.Column(db.String(16))
    cases_id = db.Column(db.String(320))
    user_id = db.Column(db.String(320))
    name = db.Column(db.String(1600))
    case_count = db.Column(db.String(64))
    how_long = db.Column(db.String(64))
    report_path = db.Column(db.String(6400))
    created_at = db.Column(db.DATETIME)
    end_at = db.Column(db.DATETIME)
    deleted_at = db.Column(db.DATETIME)
    status = db.Column(db.String(3),comment='1:运行中 2运行完成 3运行失败')

    def __init__(self, project_id, cases_id, name, case_count,allure_report_path):
        self.project_id = project_id
        self.cases_id = cases_id
        self.case_count = case_count
        self.name = name
        self.created_at = datetime.now()
        self.how_long = '0'
        self.status = '1'
        self.report_path = allure_report_path

    def __repr__(self):
        return '<Job %r>' % self.name