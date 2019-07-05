from app import app
from flask import render_template, redirect, url_for, request, abort, flash
from app import mysql
from app.models.login import loginForm, User
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

#Mostra as modalidades de jogos
@app.route("/home/categorias")
def categorias():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT tbmodalidade_nome FROM tb_modalidade''')
    dadosobtidos = cur.fetchall()
    dadosobtidos = list(dadosobtidos)
    tamanho2 = len(dadosobtidos)
    lista2 = []
    #array para passar de parametro para o html, contendo o nome dos jogadores sem time
    for i in range(0, tamanho2):
        lista2.append(str(dadosobtidos[i][0]))
    cur.close()
    return render_template("categoria.html", lista2= lista2, tamanho2=tamanho2)

@app.route("/home/dota2", methods = ["GET", "POST"])
def dota2():
    # query para obter o nome dos campeonatos da modalidade dota2
    cur = mysql.connection.cursor()
    cur.execute('''SELECT tbcampeonato_nome FROM tb_campeonato where tbcampeonato_modalidade = 1''')
    dadosobtidos = cur.fetchall()
    dadosobtidos = list(dadosobtidos)
    tamanho2 = len(dadosobtidos)
    lista2 = []
    #array para passar de parametro para o html
    for i in range(0, tamanho2):
        lista2.append(str(dadosobtidos[i][0]))
    # query para montar a tabela das partidas de um dado campeonato
    lista = []
    for j in range(0, tamanho2): # arrumar o for para tamanho2
        print(lista2[j])
        cur.execute('''select tb_time.tbtime_nome from tb_time inner join tb_partida on tb_time.tbtime_id = tb_partida.tbpartida_time1 inner join tb_campeonato on tb_partida.tbpartida_campeonato = tb_campeonato.tbcampeonato_id where tb_campeonato.tbcampeonato_nome = %s order by tbpartida_id;''', (lista2[j],))
        dadosobtidos = cur.fetchall()
        dadosobtidos = list(dadosobtidos)
        tamanhotime1 = len(dadosobtidos)        
        time1 = []
        for k in range(0, tamanhotime1):
            time1.append(str(dadosobtidos[k][0]))
            print(dadosobtidos[k][0])
        lista.append(time1)
        lista.append(tamanhotime1)
        cur.execute('''select tb_time.tbtime_nome from tb_time inner join tb_partida on tb_time.tbtime_id = tb_partida.tbpartida_time2 inner join tb_campeonato on tb_partida.tbpartida_campeonato = tb_campeonato.tbcampeonato_id where tb_campeonato.tbcampeonato_nome = %s order by tbpartida_id;''', (lista2[j],))
        dadosobtidos = cur.fetchall()
        dadosobtidos = list(dadosobtidos)
        tamanhotime1 = len(dadosobtidos)        
        time1 = []
        for k in range(0, tamanhotime1):
            time1.append(str(dadosobtidos[k][0]))
        lista.append(time1)
        lista.append(tamanhotime1)
        print(lista)
    cur.close()
    return render_template("dota2.html", lista2= lista2, tamanho2=tamanho2, lista=lista)

#@app.route("/home/campeonatos", methods=["GET", "POST"])

#def campeonatos():
    
