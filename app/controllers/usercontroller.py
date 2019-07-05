from app import app
from flask import render_template, redirect, url_for, request
from app import mysql
from app.models.user import userForm
import hashlib

@app.route("/home/novaACC", methods=["GET","POST"])
def user1():
    form = userForm()
    if request.method == "POST":
        nome1 = request.form['nome']
        senha1 = request.form['senha']
        ############################################################################
        # inserindo no banco de dados
        time = 1 # nao pode ser 0, pois o banco comeca em 0
        tipo1 = 1
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO tb_user (tbuser_nome, tbuser_senha, tbuser_time, tbuser_tipo) VALUES (%s, %s, %s, %s)''', (nome1, senha1, int(time), int(tipo1)))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("index")) #nome do metodo
    else:
        print ("Erro nos Formularios")

    return render_template('novaACC.html', form = form)
