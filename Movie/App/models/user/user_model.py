import datetime

from App.exts import db
from App.models import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    userlogs = db.relationship('UserLog', backref='user')  # 会员日志外键关系关联，backref互相绑定user表
    comments = db.relationship('Comment', backref='user')  # 用户评论外键关系关联
    moviecollects = db.relationship('MovieCollect', backref='user')  # 用户收藏电影外键关系关联
