from App.views.admin import blue_admin
from App.views.home import blue_home


def init_blue(app):
    app.register_blueprint(blue_admin, url_prefix="/admin")
    app.register_blueprint(blue_home)
