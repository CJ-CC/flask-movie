import datetime

from App.exts import db
from App.models import BaseModel


# 权限
class Auth(BaseModel):
    __tablename__ = 'auth'
    name = db.Column(db.String(100), unique=True)  # 权限名称
    url = db.Column(db.String(255), unique=True)  # 权限地址
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间