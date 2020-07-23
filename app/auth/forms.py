from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField, PasswordField, SelectField, FileField
from wtforms.validators import Email, Length, DataRequired, ValidationError, InputRequired, EqualTo
from wtforms.fields.html5 import EmailField
from app.auth.models import User
from flask_wtf.file import FileAllowed
import os,app
from os import walk


def galleryPics():
    directory = os.path.join(os.getcwd(),'app','static','files')
    allpics =[]
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".PNG") or filename.endswith(".JPG"):
            allpics.append( filename)
            #os.path.join(directory,

   
    return allpics



def save_pic(file_name, category,pic_name):
    f_name, f_ext = os.path.splitext(file_name.filename)
    img_name = category + "_" + f_name + "_" + f_ext
    img_path = os.path.join(os.getcwd(),'app/static/files',img_name)
    file_name.save(img_path)
    return img_name

def check_email(form, field):
    
        user_exist = User.query.filter_by(username = field.data).first()
        if user_exist:
            raise ValidationError('email already exist')

def check_email_login(form, field):
    
        user_exist = User.query.filter_by(username = field.data).first()
        if not user_exist:
            raise ValidationError('email does not exist, please register to gain access.')

class ContactUs(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email',validators = [InputRequired(),
    Email(message="please enter a valid email format")])
    message = TextAreaField('Message', validators= [DataRequired() ,Length(max=200 )],render_kw={"rows": 10, "cols": 11})
    submit = SubmitField('Submit')

class PictureUpload(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email',validators = [InputRequired(),Email(message="please enter a valid email format")])
    message = TextAreaField('Message', validators= [DataRequired() ,Length(max=200 )],render_kw={"rows": 10, "cols": 11})
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Email',validators = [InputRequired(),Email(message="please enter a valid email format"),check_email_login])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class NewUserForm(FlaskForm):
    username = StringField('Email',validators = [InputRequired(),Email(message="please enter a valid email format"),check_email])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message = 'password must match')])
    role = SelectField('Role', choices=[('Administrator','Administrator')])
    submit = SubmitField('Submit')

class FormUpload(FlaskForm):
    picname = StringField('Name', validators = [DataRequired()])
    category = SelectField('Category', choices=[('Birthday','Birthday'),('Wedding', 'Wedding')])
    #description= TextAreaField('Description', validators= [DataRequired() ,Length(max=200 )],render_kw={"rows": 10, "cols": 11})
    file = FileField('Upload Picture', validators= [FileAllowed(['jpg','png'])])
    submit = SubmitField('Submit')