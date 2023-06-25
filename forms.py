from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class Payment(FlaskForm):
    card_number = StringField('Card Number', validators=[DataRequired()])
    card_holder = StringField('Card Holder', validators=[DataRequired()])
    expiration_month = IntegerField('Expiration Month', validators=[DataRequired()])
    expiration_year = IntegerField('Expiration year', validators=[DataRequired()])
    cvv = IntegerField('CVV', validators=[DataRequired()])
    pay = SubmitField('Pay')







