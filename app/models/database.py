from app.models import db
from datetime import datetime

class Database(db.Model):
    # 定义表名
    __tablename__ = "databases"

    id = db.Column(db.INT,primary_key=True)
    name = db.Column(db.String(16),index=True)
    host = db.Column(db.String(16),index=True)
    port = db.Column(db.INT, nullable=False)
    username = db.Column(db.String(16), index=True)
    password = db.Column(db.String(32))
    database_name = db.Column(db.String(32))
    connect_status = db.Column(db.String(3200),comment="连接状态")
    sql_type = db.Column(db.INT, default=0, comment="0: mysql 1: postgresql 2: mongo")
    created_at = db.Column(db.DATETIME, nullable=False)
    updated_at = db.Column(db.DATETIME, nullable=False)
    deleted_at = db.Column(db.DATETIME)
    create_user = db.Column(db.String(32))

    def __init__(self, name,host,port,username, password,database_name , create_user,sql_type=0,connect_status="fail"):
        self.name = name
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database_name = database_name
        self.create_user = create_user
        self.sql_type = sql_type
        self.connect_status = connect_status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return '<Database %r>' % self.id