import datetime

from App.exts import db
from App.models import BaseModel



class Admin(BaseModel):
    __tablename__ = 'admin'
    name = db.Column(db.String(100), unique=True)  # 管理员账号
    pwd = db.Column(db.String(100))  # 密码
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员，0为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属角色
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
    adminlogs = db.relationship('AdminLog', backref='admin')  # 管理员日志外键关系关联，backref互相绑定admin表
    operatelogs = db.relationship('OperateLog', backref='operatelog')  # 管理员操作日志外键关系关联