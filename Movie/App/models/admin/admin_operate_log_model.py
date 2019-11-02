import datetime

from App.exts import db
from App.models import BaseModel


class OperateLog(BaseModel):
    __tablename__ = "operatelog"
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录ip
    reason = db.Column(db.String(600))  # 操作原因
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 时间
