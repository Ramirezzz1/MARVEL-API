from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class newAvengerForm(FlaskForm):
    hero = StringField('Hero',validators=[DataRequired()])
    firstname = StringField('First Name',validators=[DataRequired()])
    lastname = StringField('Last Name',validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    hometown = StringField('Hometown')
    powers = StringField('Powers', validators=[DataRequired()])
    weaknesses = StringField('Weaknesses', validators=[DataRequired()])
    submit = SubmitField()
    
class loginform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()

class SignUpform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField()