from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # do stuff
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password')
        password2 = request.form.get('confirmation')

        if len(username) < 3:
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
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("signup.html")
