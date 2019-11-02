import datetime

from App.exts import db
from App.models import BaseModel


class UserLog(BaseModel):
    __tablename__ = "userlog"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 登录IP
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 登录时间
