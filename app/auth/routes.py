# app/auth/routes

from app.auth import auth
from flask import render_template, url_for, redirect


@auth.route("/index")
def index():
    return render_template('index.html', title='Landing_Page')


@auth.route("/home")
def home():
    return render_template('home.html', title='Home')


@auth.route("/about")
def about():
    return render_template('about.html', title='About')

@auth.route("/gallery")
def gallery():
    return render_template('gallery.html', title='gallery')


@auth.route("/pricelist")
def pricelist():
    return render_template('pricelist.html', title='pricelist')


@auth.route("/contactus")
def contactus():
    return render_template('contactus.html', title='contactus')