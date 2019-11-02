from flask import Flask

from App.exts import init_ext
from App.settings import envs
from App.views import init_blue


def create_app(env):
    app = Flask(__name__)
    # 初始化第三方插件
    # 初始化配置
    app.config.from_object(envs.get(env))
    init_ext(app)
    # 初始化蓝图
    init_blue(app)
    return app
