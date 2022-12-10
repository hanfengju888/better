from app.models import db
from datetime import datetime

class Mock(db.Model):
    id = db.Column(db.INT,primary_key=True)
    name = db.Column(db.String(16))
    path = db.Column(db.String(64))
    method = db.Column(db.String(64))
    header = db.Column(db.String(6400))
    body = db.Column(db.String(6400))
    response_data = db.Column(db.String(6400))
    status = db.Column(db.String(16),comment="1：开启  2：关闭")
    use_count = db.Column(db.INT)
    created_at = db.Column(db.DATETIME, nullable=False)
    updated_at = db.Column(db.DATETIME, nullable=False)
    deleted_at = db.Column(db.DATETIME)

    def __init__(self,name,path,method,header,body, response_data):
        self.name = name
        self.path = path
        self.method = method
        self.header = header
        self.body = body
        self.response_data = response_data
        self.use_count = 0
        self.status = '1'
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return '<Mock %r>' % self.name