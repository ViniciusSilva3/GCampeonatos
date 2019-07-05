from app import app
from flask import render_template, redirect, url_for, request
from app import mysql
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

#app.config.from_object('config') #seta as configuracoes


@app.route("/home/menu", methods=["GET","POST"])
def menu():
    if current_user.is_authenticated:
        return render_template('menu.html', title = current_user.nome)
    else:
        return render_template('home.html')
