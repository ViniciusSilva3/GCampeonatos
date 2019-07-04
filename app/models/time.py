from app import mysql
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class TimeForm(FlaskForm):
    timeid = IntegerField("timeid") #nao sei se precisa
    nome = StringField("nome", validators=[DataRequired()])
    modalidade = IntegerField("modalidade")
    jogador2 = StringField("jogador2", validators=[DataRequired()])
    jogador3 = StringField("jogador3", validators=[DataRequired()])
    jogador4 = StringField("jogador4", validators=[DataRequired()])
    jogador5 = StringField("jogador5", validators=[DataRequired()])
    submit = SubmitField('Submit Local')
