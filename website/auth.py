from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/verihiddenpagenooneknows')
def verihiddenpagenooneknows():
    return render_template("verihiddenpage.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do stuff
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first() # get the first user with the username
        if user : 
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else :
                flash('Incorrect password, try again.', category='error')
        else :
            flash('Username does not exist.', category='error')


    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # do stuff
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password')
        password2 = request.form.get('confirmation')

        user = User.query.filter_by(username=username).first() # get the first user with the username
        if user :
            flash('Username already exists.', category='error')
        elif len(username) < 3:
            flash ('Username must be greater than 3 characters.', category='error')
        elif len(firstname) < 3:
            flash ('First name must be greater than 3 characters.', category='error')
        elif len(lastname) < 3:
            flash ('Last name must be greater than 3 characters.', category='error')
        elif password != password2:
            flash ('Passwords don\'t match.', category='error')
        elif len(password) < 8:
            flash ('Password must be at least 8 characters.', category='error')
        else:
            # add user to database
            new_user = User(username=username, firstname=firstname, lastname=lastname, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))
        
    return render_template("signup.html", user = current_user)

