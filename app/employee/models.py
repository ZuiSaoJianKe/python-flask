from RealProject import db, mongo,fds,mail
from common.baseModels import BaseModel


class EmployeeModel(BaseModel):
    __tablename__ = 'employee'
    # __bind_key__ = 'other'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), unique=False)
    pswd = db.Column(db.String(32), unique=False)
    is_delete = db.Column(db.Integer, unique=False)
    mail = db.Column(db.String(32), unique=False)
    # position_id= db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)


class User(mongo.Document):
    name = mongo.StringField()
    password = mongo.StringField()


class Employee(mongo.Document):
    name = mongo.StringField()




