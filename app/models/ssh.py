from app.models import db
from datetime import datetime

class Ssh(db.Model):
    id = db.Column(db.INT,primary_key=True)
    name = db.Column(db.String(16))
    ip = db.Column(db.String(64))
    port = db.Column(db.String(64))
    cpu = db.Column(db.String(64))
    mem = db.Column(db.String(64))
    disk = db.Column(db.String(64))
    process_number = db.Column(db.String(64))
    username = db.Column(db.String(16))
    password = db.Column(db.String(32))
    created_at = db.Column(db.DATETIME, nullable=False)
    updated_at = db.Column(db.DATETIME, nullable=False)
    deleted_at = db.Column(db.DATETIME)

    def __init__(self,name,ip,port, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.ip = ip
        self.port = port
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return '<Ssh %r>' % self.name