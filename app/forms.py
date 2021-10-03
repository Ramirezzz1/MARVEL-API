from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class newAvengerForm(FlaskForm):
    hero = StringField('Hero',validators=[DataRequired()])
    firstname = StringField('First Name',validators=[DataRequired()])
    lastname = StringField('Last Name',validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    hometown = StringField('Hometown')
    powers = StringField('Powers', validators=[DataRequired()])
    weaknesses = StringField('Weaknesses', validators=[DataRequired()])
    submit = SubmitField()
    
