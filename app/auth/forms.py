from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField
from wtforms.validators import Email, Length, DataRequired

class ContactUs(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email',validators = [Email(), DataRequired()])
    phone_number = StringField('Phone Number', validators= [])
    message = TextAreaField('Message', validators= [DataRequired() ,Length(max=200 )],render_kw={"rows": 10, "cols": 11})
    submit = SubmitField('Submit')

