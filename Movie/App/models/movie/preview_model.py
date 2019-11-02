import datetime

from App.exts import db
from App.models import BaseModel


class Preview(BaseModel):
    __tablename__ = 'preview'
    title = db.Column(db.String(255), unique=True)  # 标题
    logo = db.Column(db.String(255), unique=True)  # 封面
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
