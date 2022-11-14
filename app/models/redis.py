from app.models import db
from datetime import datetime

class Redis(db.Model):
    # 定义表名
    __tablename__ = "redis"

    id = db.Column(db.INT,primary_key=True)
    env = db.Column(db.INT)
    name = db.Column(db.String(256))
    addr = db.Column(db.String(256))
    host = db.Column(db.String(16))
    port = db.Column(db.String(16))
    password = db.Column(db.String(320))
    db_number = db.Column(db.INT)
    key_count = db.Column(db.String(32))
    cluster = db.Column(db.INT,default=0,comment="是否是集群,0为否 1为是 集群则不用输入用户名密码")
    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)
    deleted_at = db.Column(db.DATETIME)

    def __init__(self, env,name,addr,host,port, password,db_number , cluster,key_count):
        self.name = name
        self.env = env
        self.addr = addr
        self.host = host
        self.port = port
        self.password = password
        self.db_number = db_number
        self.cluster = cluster
        self.key_count = key_count
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return '<Redis %r>' % self.id