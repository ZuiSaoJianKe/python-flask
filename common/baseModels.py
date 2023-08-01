from RealProject import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
