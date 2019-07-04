from app import mysql
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

class loginForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    senha = StringField("senha", validators=[DataRequired()])
    submit = SubmitField('Submit Local')

class User(UserMixin):
    def __init__(self, id1, nome1, tipo1, time1, active):
        self.id = id1
        self.nome = nome1
        self.tipo = tipo1
        self.time = time1
        self.active = active
    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

