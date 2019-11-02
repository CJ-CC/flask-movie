import datetime

from App.exts import db
from App.models import BaseModel


class Role(BaseModel):
    __tablename__ = 'role'
    name = db.Column(db.String(100), unique=True)  # 角色名称
    auths = db.Column(db.String(600))  # 权限列表
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
    admins = db.relationship('Admin', backref='role')  # 管理员外键关系关联，backref互相绑定role表