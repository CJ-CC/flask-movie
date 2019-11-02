import datetime

from App.exts import db
from App.models import BaseModel


class MovieCollect(BaseModel):
    __tablename__ = 'moviecollect'
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影，在movie表中创建关联
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户，在user表中创建外键关联
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间