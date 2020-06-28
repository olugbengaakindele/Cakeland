from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField
from wtforms.validators import Email, Length, DataRequired, ValidationError



'''
def check_email(form, field):
        #email_exist = Users.query.filter_by(user_email=field.data).first()
        if email_exist:
            raise ValidationError(
                'email already exist, please go to login page')

'''

class ContactUs(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email',validators = [DataRequired(),Email(message="please enter a valid email format")])
    message = TextAreaField('Message', validators= [DataRequired() ,Length(max=200 )],render_kw={"rows": 10, "cols": 11})
    submit = SubmitField('Submit')

