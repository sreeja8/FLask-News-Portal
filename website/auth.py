from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #to encrypt password
from . import db
from flask_login import login_user, login_required, logout_user, current_user #to access all info about the currently loggin in user

auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email not in ["sreejaAdmin@yahoo.com", "johnAdmin@yahoo.com", "celinaAdmin@yahoo.com"]:
            flash("Account doesn't have editor access", category='error')
            return redirect(url_for("views.home"))

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True) #logs in user, and remembers user unless the user clears their browsing history or web server restarts
                return redirect(url_for('views.editor_news'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')


    return render_template("login.html", user=current_user) #variable="Testing", user="Sreeja") #passing value Testing via a variable name "variable"

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/editor_corner/sign-up' , methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name1 = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first() #checking the db User to see if email/user already exists

        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name1) <2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) <7:
            flash('Password must be atleast 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name1, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))


    return render_template("sign_up.html", user=current_user)