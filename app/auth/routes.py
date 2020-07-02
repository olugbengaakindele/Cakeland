# app/auth/routes

from app.auth import auth
from app import db, bcrypt
from app.auth.models import Visits
from flask import render_template, url_for, redirect, session, g, flash
from app.auth.forms import ContactUs, PictureUpload, LoginForm, NewUserForm
from datetime import datetime
from app.auth.models import User


@auth.route("/index")
def index():
    visit_count = Visits(count=1, visit_date=datetime.utcnow())
    db.session.add(visit_count)
    db.session.commit()
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


@auth.route("/training")
def training():
    return render_template('training.html', title='training')


@auth.route("/contactus", methods=["GET", "POST"])
def contactus():
    form = ContactUs()

    if form.validate_on_submit():
        flash("Message saved")
        return redirect(url_for('auth.home'))
    else:
        return render_template('contactus.html', title='contactus', form=form)

    return render_template('contactus.html', title='contactus', form=form)


@auth.route("/adminlogin", methods=['POST', 'GET'])
def adminlogin():
    form = LoginForm()
    return render_template('adminlogin.html', title='admin_login', form=form)


@auth.route("/adminnewuser", methods=['POST', 'GET'])
def adminnewuser():
    form = NewUserForm()
    if form.validate_on_submit():
        User.create_user(form.username.data, form.password.data, form.role.data)
        return redirect(url_for('auth.adminlogin'))

    return render_template('adminnewuser.html', title='register_user', form=form)
