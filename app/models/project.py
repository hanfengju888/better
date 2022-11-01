import random

from app.models import db
from datetime import datetime
from app import better


class Project(db.Model):
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String(16), unique=True, index=True)
    owner = db.Column(db.INT)
    created_at = db.Column(db.DATETIME, nullable=False)
    updated_at = db.Column(db.DATETIME, nullable=False)
    deleted_at = db.Column(db.DATETIME)
    create_user = db.Column(db.INT, nullable=True)
    update_user = db.Column(db.INT, nullable=True)
    private = db.Column(db.INT,comment="0:False 1:True")
    img = db.Column(db.String(1024))

    def __init__(self, name, owner, create_user, private=0):
        self.name = name
        self.owner = owner
        self.private = private
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.create_user = create_user
        self.update_user = create_user
        self.deleted_at = None
        self.img = random.choice(better.config.get("PROJECT_IMG_LIST"))