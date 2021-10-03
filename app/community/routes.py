#Instantiate Blueprint
from inspect import FullArgSpec
from flask import Blueprint,render_template,request
from flask.helpers import flash, url_for, flash
from flask_wtf.recaptcha import validators
from werkzeug.utils import redirect
from app.forms import newAvengerForm
from app.models import Avenger

community = Blueprint('community', __name__, template_folder='community_templates')

@community.route('/community')
def ourcommunity():
    return render_template('community.html')

@community.route('/addavenger', methods=['GET','POST'])
def add_avenger():
    form=newAvengerForm()
    if request.method =='POST':
        if form.validate_on_submit():
            print('New avenger added')


            #instance of our actor object from form data
            newavenger = Avenger(
                hero=form.hero.data,
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                age=form.age.data,
                hometown=form.hometown.data,
                powers=form.powers.data,
                weaknesses=form.weaknesses.data)
            db.session.add(newavenger)
            db.session.commit()

            flash('New Avenger added to our database.', category='alert-info')
            flash(f'{newavenger.to_dict()}', category='alert-info')
        else:
            flash('Invalid Credentials please try again ', category='alert-danger')
    return render_template('addavenger.html',form=form)