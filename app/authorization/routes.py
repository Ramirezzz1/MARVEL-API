import re
from flask import Blueprint, render_template, redirect, request, flash, url_for
from app.forms import SignUpform, loginform 
from werkzeug.security import check_password_hash
from flask_login import login_user , logout_user
from app.models import db, User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup',methods=['GET','POST'])
def signup():
    form = SignUpform()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(form.username.data, form.password.data, form.email.data, form.first_name.data, form.last_name.data)

            db.session.add(new_user)
            db.session.commit()

            flash(f'Congratulations and Welcome: {form.username.data}')
            login_user(new_user)
            return redirect(url_for('home'))
        else:
            flash('Invalid input, try again ', category= 'alert-danger')
            return redirect(url_for('auth.signup'))
    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET','POST'])
def login():
    form = loginform()
    if request.method == 'POST':
        if form.validate_on_submit():
            usernamedata = form.username.data
            passworddata = form.password.data 
            user = User.query.filter_by(username=usernamedata).first()
            if user is None or not check_password_hash(user.password, passworddata):
                flash('Incorrect login Credentials', category= "alert-danger")
                return redirect(url_for('auth.login'))

            login_user(user)
            flash(f'Welcome back Avenger!')
            return redirect(url_for('home'))
        else:
            flash('You do not have access, please try again.', category='alert-danger')
            return redirect(url_for('auth.login'))
    return render_template('login.html', form = form )


@auth.route('/logout', methods=['GET'])
def signout():
    logout_user()
    flash('See you soon !', category='alert-info')
    return redirect(url_for('auth.signin'))