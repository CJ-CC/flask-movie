

from App.exts import db
from App.models import BaseModel



# 电影
import datetime


class Movie(BaseModel):
    __tablename__ = 'movie'
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 播放地址
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    play_num = db.Column(db.BigInteger)  # 播放量
    comment_num = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 播放时长
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
    comments = db.relationship('Comment', backref='movie')  # 用户评论外键关系关联
    moviecollects = db.relationship('MovieCollect', backref='movie')  # 用户收藏电影外键关系关联