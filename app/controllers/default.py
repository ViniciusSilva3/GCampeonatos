from app import app
from flask import render_template, redirect, url_for, request
from app import mysql
from app.models.local import LocalForm

#app.config.from_object('config') #seta as configuracoes
@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/home/local", methods=["GET","POST"])
def Local():
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
        return redirect(url_for("index")) #nome do metodo
    else:
        print ("Erro nos Formularios")

    return render_template('local.html', form = form)

