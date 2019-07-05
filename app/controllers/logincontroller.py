from app import app
from flask import render_template, redirect, url_for, request, abort, flash
from app import mysql
from app.models.login import loginForm, User
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import hashlib

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader

def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT tbuser_id, tbuser_nome, tbuser_tipo, tbuser_time FROM tb_user WHERE tbuser_id = %s''', (user_id,))
    dadosobtidos = cur.fetchall()
    dadosobtidos = list(dadosobtidos)
    cur.close()
    print(dadosobtidos[0][0])
    return User(dadosobtidos[0][0], dadosobtidos[0][1], dadosobtidos[0][2], dadosobtidos[0][3], True)
#@app.route("/")
@app.route("/home/login", methods=["GET","POST"])

def login():
    form = loginForm()
    if request.method == "POST":
        nome1 = request.form['nome']
        senha1 = request.form['senha']
        ############################################################################
        # inserindo no banco de dados
        cur = mysql.connection.cursor()
        cur.execute('''SELECT tbuser_nome, tbuser_senha, tbuser_id FROM tb_user WHERE tbuser_nome = %s''', (nome1,))
        dadosobtidos = cur.fetchall()
        dadosobtidos = list(dadosobtidos)
        cur.close()
        if nome1 == dadosobtidos[0][0] and senha1 == dadosobtidos[0][1]:
            
            user = load_user(dadosobtidos[0][2])
            login_user(user)
            flash('Logged in successfully')
            #next = flask.request.args.get('next')
            return redirect(url_for("menu")) #nome do metodo
        return abort(400)
    else:
        print ("Erros nos Forms")

    return render_template('login.html', form = form)

@app.route("/home/logout", methods=["GET","POST"])
def logout():
    logout_user()
    return redirect(url_for("index"))

