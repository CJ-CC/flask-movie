from App.exts import db


class BaseModel(db.Model):
    # 定义__abstract__方便继承，不生成BaseModel表
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
