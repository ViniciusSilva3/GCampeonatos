from app import mysql
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class userForm(FlaskForm):
    userid = IntegerField("userid") #nao sei se precisa
    nome = StringField("nome", validators=[DataRequired()])
    senha = StringField("senha", validators=[DataRequired()])
    tipo = IntegerField("tipo")
    time = IntegerField("time")
    submit = SubmitField('Submit Local')
