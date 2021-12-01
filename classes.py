
from wtforms import Form, StringField, PasswordField, validators, TextAreaField, EmailField
from wtforms.widgets import TextArea
import datetime

# The authentication and registeration method has been learned from this tutorial on
# https://www.youtube.com/watch?v=addnlzdSQs4 and wtforms documentation.
class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25),
                            validators.DataRequired(), validators.Regexp('^\w+$',
                            message="Username must contain only letters numbers or underscore")])
    location = StringField('Your Location', [validators.Length(min=3, max=50), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(min=6, max=50), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')

    ])
    confirm = PasswordField('Confirm Password')


class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')



class ReviewForm(Form):
    review = StringField('Write Here', widget=TextArea())
    created_date = datetime.datetime.now() 



class EditProfile(Form):
    username = StringField('Username', [validators.Length(min=4, max=25),
                            validators.DataRequired(), validators.Regexp('^\w+$',
                            message="Username must contain only letters numbers or underscore")])
    location = StringField('Your Location', [validators.Length(min=3, max=50), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(min=6, max=50), validators.DataRequired()])

