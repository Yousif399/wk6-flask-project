from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class Signup(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Passwords', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    signup = SubmitField()


class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Passwords', validators=[DataRequired()])
    signup = SubmitField()
