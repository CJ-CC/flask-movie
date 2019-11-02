import datetime

from App.exts import db
from App.models import BaseModel


# 管理员日志
class AdminLog(BaseModel):
    __tablename__ = "adminlog"
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 登录时间
