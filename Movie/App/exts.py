# 第三方插件统一使用懒加载方式,
# 邮件验证
from flask_mail import Mail
# 数据库orm
from flask_sqlalchemy import SQLAlchemy
# 数据库迁移
from flask_migrate import Migrate
# 缓存
from flask_caching import Cache

# 先创建对象，等到要使用的时候再进行初始化
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
# 缓存方式选择redis
cache = Cache(
    config={
        'CACHE_TYPE': "redis"
    }
)


def init_ext(app):
    """
    第三方插件通常都要传入一个app参数
    :param app:
    :return:
    """
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    cache.init_app(app)
