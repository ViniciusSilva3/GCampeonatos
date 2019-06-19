from app import app
from flask import render_template, redirect, url_for, request
from app import mysql
from app.models.local import LocalForm
from flask-login import LoginManager

#login_manager = LoginManager()
#login_manager.init_app(app)
#@app.route("/")
#@app.route("/home/login")
#def login():


