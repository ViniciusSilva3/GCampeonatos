from app import app
from flask import render_template, redirect, url_for, request
from app import mysql
from app.models.local import LocalForm
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

#app.config.from_object('config') #seta as configuracoes
@app.route("/")
@app.route("/home", methods=["GET","POST"])
def index():
    return render_template("home.html")

@app.route("/home/local", methods=["GET","POST"])
def Local():
    if current_user.is_authenticated:
        form = LocalForm()
        if request.method == "POST":
            nome1 = request.form['nome']
            cidade1 = request.form['cidade']
            capacidade1 = request.form['capacidade']
            # inserindo no banco de dados
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO tb_local (tblocal_nome, tblocal_cidade, tblocal_capacidade) VALUES (%s, %s, %s)''', (nome1, cidade1, capacidade1))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for("menu")) #nome do metodo
        else:
            print ("Erro nos Formularios")
    else:
        render_template('home.html')
    return render_template('local.html', form = form)

