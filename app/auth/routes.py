# app/auth/routes

from app.auth import auth
from app import db, bcrypt
from app.auth.models import Visits
from flask import render_template, url_for, redirect, session, g, flash
from app.auth.forms import ContactUs, PictureUpload, LoginForm, NewUserForm,FormUpload,save_pic
from datetime import datetime
from app.auth.models import User
from app import loginmanager
from flask_login import login_user,login_required



@auth.route("/index")
def index():
    visit_count = Visits(count=1, visit_date=datetime.utcnow())
    db.session.add(visit_count)
    db.session.commit()
    return render_template('index.html', title='Landing_Page')


@auth.route("/home", methods = ["POST", "GET"])
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
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for("auth.dashboard"))  

        else:
            flash("Message saved")
            return redirect(url_for('auth.adminlogin'))

    
    return render_template('adminlogin.html', title='admin_login', form=form)


@auth.route("/adminnewuser", methods=['POST', 'GET'])
def adminnewuser():
    form = NewUserForm()
    if form.validate_on_submit():
        User.create_user(form.username.data, form.password.data, form.role.data)
        return redirect(url_for('auth.adminlogin'))

    return render_template('adminnewuser.html', title='register_user', form=form)


@auth.route("/admin/dashboard", methods= ["GET","POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", title = "Dashbaord")

@auth.route("/admin/upload", methods= ["GET","POST"])
def upload():
    form = FormUpload()
    if form.validate_on_submit():
        pic_name = save_pic(form.file.data,form.category.data,'lk')
        return render_template("upload.html", title = "uploads", form= form)
    
    return render_template("upload.html", title = "uploads", form= form)