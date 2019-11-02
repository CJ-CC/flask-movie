from flask import Blueprint, render_template, redirect, url_for

blue_home = Blueprint("home", __name__)


@blue_home.route('/')
def index():
    return render_template('home/index.html')


@blue_home.route('/login/')
def login():
    return render_template('home/login.html')


@blue_home.route('/logout/')
def logout():
    return redirect(url_for('home.login'))


@blue_home.route('/register/')
def register():
    return render_template('home/register.html')


@blue_home.route('/user/')
def user():
    return render_template('home/user.html')


@blue_home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')


@blue_home.route('/comments/')
def comments():
    return render_template('home/comments.html')


@blue_home.route('/userlog/')
def userlog():
    return render_template('home/userlog.html')


@blue_home.route('/moviecollect/')
def moviecollect():
    return render_template('home/moviecollect.html')
