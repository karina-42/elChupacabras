from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Sign in an existing user: get the input from the form and validate it

    :return: A redirection to the home page if successful, or to the login
    html template if not.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully! Hello!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again.',
                      category='error')
        else:
            flash('User does not exist, please create an account.',
                  category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    """
    Logout the user if they are logged in

    :return: A redirection to the login html template
    """
    logout_user()
    flash('Logged out successfully! See you!', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    Register a new user: get data from the form, validate the input, create
    a new user, then redirect to the home page.

    :return: A redirection to home if successful, or to the sign-up html
    template if not.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user_email = User.query.filter_by(email=email).first()
        user_username = User.query.filter_by(username=username).first()
        if user_email:
            flash('Email already exists', category='error')
        elif user_username:
            flash('Username is already taken', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.',
                  category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            try:
                new_user = User(email=email,
                                password=generate_password_hash(password1),
                                username=username)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
            except Exception as e:
                print(f"Error adding user record: {e}")
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
