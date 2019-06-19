from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
#Mysql configs:

app.config['MYSQL_USER'] = 'vsilva13'
app.config['MYSQL_PASSWORD'] = 'nv8735qw'
app.config['MYSQL_DB'] = 'GCampeonatos'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

app.config['SECRET_KEY'] = "felipeayres"



from app.controllers import default
from app.controllers import usercontroller
