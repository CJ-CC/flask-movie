import os


def get_db_uri(dbinfo):
    ENGINE = dbinfo.get('ENGINE')
    DRIVER = dbinfo.get('DRIVER')
    USER = dbinfo.get('USER')
    PASSWORD = dbinfo.get('PASSWORD')
    HOST = dbinfo.get('HOST')
    PORT = dbinfo.get('PORT')
    NAME = dbinfo.get('NAME')

    return "{}+{}://{}:{}@{}:{}/{}".format(
        ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME
    )


# 配置父类，用过继承该类实现不同的环境
class config:
    TESTING = False

    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'CC'


class DevelopConfig(config):
    DEBUG = True
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'qbk95ak47',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'movie'

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


# 配置一个字典，从环境变量中获取对应的值，可以适配不同的环境。比如开发、测试、演示、产品。
envs = {
    "develop": DevelopConfig,
    # 'testing':Testing
    'default': DevelopConfig
}

ADMINS = ['lcj', 'lsy']
FILE_PATH_PREFIX = '/static/uploads/icons/'
# BASE_DIR = r'‪E:\pychram-workplace\FlaskTpp'
BASE_DIR = os.getcwd()
UPLOADS_DIR = os.path.join(BASE_DIR, 'App/static/uploads/icons')
