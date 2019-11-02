from flask import Blueprint

blue_admin = Blueprint("admin", __name__)


@blue_admin.route('/')
def admin():
    return "<h1 style='color:blue'>后台</h1>"
