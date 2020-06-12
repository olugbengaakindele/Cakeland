# app/auth/routes

from app.auth import auth
from flask import render_template, url_for, redirect


@auth.route("/index")
def index():
    return render_template('index.html', title='Home')
