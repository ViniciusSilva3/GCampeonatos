from app import app
from flask import render_template, redirect, url_for, request
from app import mysql
from app.models.user import userForm
import hashlib

@app.route("/home/novaACC", methods=["GET","POST"])
def user():
    form = userForm()
    if request.method == "POST":
        nome1 = request.form['nome']
        senha1 = request.form['senha']
        # a sequencia a seguir serve para gerar um hash para a senha a ser inserida
        salt = "a8kl"
        db_password = senha1 + salt
        h = hashlib.md5(db_password.encode())
        ############################################################################
        # inserindo no banco de dados
        tipo = 1
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO tb_user (tbuser_nome, tbuser_senha, tbuser_time) VALUES (%s, %s, %s)''', (nome1, h, int(tipo)))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("index")) #nome do metodo
    else:
        print ("Erro nos Formularios")

    return render_template('novaACC.html', form = form)
