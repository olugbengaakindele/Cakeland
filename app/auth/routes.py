# app/auth/routes

from app.auth import auth
from app import db
from app.auth.models import Visits
from flask import render_template, url_for, redirect, session, g,flash
from app.auth.forms import ContactUs, PictureUpload
from datetime import datetime




    

@auth.route("/index")
def index():
    visit_count = Visits(count= 1, visit_date = datetime.utcnow())
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

@auth.route("/contactus" , methods= ["GET","POST"])
def contactus():
    form = ContactUs()

    if form.validate_on_submit():
        flash("Message saved")
        return redirect(url_for('auth.home'))
    else:
        flash("Message saved")
        return render_template('contactus.html', title='contactus', form = form)

    return render_template('contactus.html', title='contactus', form = form)

@auth.route("/admin", methods=['post','get'])
def admin():
    form = PicturUpload()
    return render_template('contactus.html', title='admin')



