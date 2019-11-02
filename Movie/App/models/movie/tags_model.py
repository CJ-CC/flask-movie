import datetime

from App.exts import db
from App.models import BaseModel


class Tag(BaseModel):
    __tablename__ = 'tag'
    name = db.Column(db.String(100), unique=True)  # 标题
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
    movies = db.relationship('Movie', backref='tag')  # 电影外键关系关联