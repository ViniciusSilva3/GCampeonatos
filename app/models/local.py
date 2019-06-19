from app import mysql
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class LocalForm(FlaskForm):
    localid = IntegerField("localid") #nao sei se precisa
    nome = StringField("nome", validators=[DataRequired()])
    cidade = StringField("cidade", validators=[DataRequired()])
    capacidade = IntegerField("capacidade", validators=[DataRequired()])
    submit = SubmitField('Submit Local')
