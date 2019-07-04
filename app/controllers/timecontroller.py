from app import app
from flask import render_template, redirect, url_for, request, abort, flash
from app import mysql
from app.models.time import TimeForm
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

@app.route("/home/novotime", methods=["GET", "POST"])
def novotime():
    if current_user.is_authenticated:
        nome1 = 1
        cur = mysql.connection.cursor()
        cur.execute('''SELECT tbuser_nome FROM tb_user WHERE tbuser_time = %s''', (nome1,))
        dadosobtidos = cur.fetchall()
        dadosobtidos = list(dadosobtidos)
        tamanho = len(dadosobtidos)
        lista = []
        #array para passar de parametro para o html, contendo o nome dos jogadores sem time
        for i in range(0, tamanho):
            lista.append(str(dadosobtidos[i][0]))
        
        cur.execute('''SELECT tbmodalidade_nome FROM tb_modalidade''')
        dadosobtidos = cur.fetchall()
        dadosobtidos = list(dadosobtidos)
        tamanho2 = len(dadosobtidos)
        print (dadosobtidos[0][0])
        lista2 = []
        #array para passar de parametro para o html, contendo o nome dos jogadores sem time
        for i in range(0, tamanho2):
            lista2.append(str(dadosobtidos[i][0]))
        cur.close()
        form = TimeForm()
        if request.method == "POST":
            nome1 = request.form['nome']
            modalidade1 = request.form['modalidade']
            jogador2 = request.form['jogador2']
            jogador3 = request.form['jogador3']
            jogador4 = request.form['jogador4']
            jogador5 = request.form['jogador5']
            # inserindo no banco de dados
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO tb_time (tbtime_nome, tbtime_modalidade) VALUES (%s, %s)''', (nome1, modalidade1,))
            mysql.connection.commit()
            cur.execute('''SELECT tbtime_id FROM tb_time where tbtime_nome = %s ''', (nome1,))
            dadosobtidos = cur.fetchall()
            dadosobtidos = list(dadosobtidos)
            timeid = dadosobtidos[0][0]
            print(timeid)
            # eh necessario alterar o time de todos os jogadores na tabela de users
            cur.execute('''update tb_user set tbuser_time = %s where tbuser_nome = (%s)''',(timeid, current_user.nome))
            mysql.connection.commit()
            cur.execute('''update tb_user set tbuser_time = %s where tbuser_nome = (%s)''',(timeid, jogador2))
            mysql.connection.commit()
            cur.execute('''update tb_user set tbuser_time = %s where tbuser_nome = (%s)''',(timeid, jogador3))
            mysql.connection.commit()
            cur.execute('''update tb_user set tbuser_time = %s where tbuser_nome = (%s)''',(timeid, jogador4))
            mysql.connection.commit()
            cur.execute('''update tb_user set tbuser_time = %s where tbuser_nome = (%s)''',(timeid, jogador5))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for("menu")) #nome do metodo
        else:
            print ("Erro nos Formularios")
    else:
        render_template('home.html')
    return render_template('time.html', form = form, lista = lista, tamanho = tamanho, lista2 = lista2, tamanho2 = tamanho2)
