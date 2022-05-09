from flask import Blueprint, render_template, redirect, url_for, request, flash
from pymongo import auth
from sqlalchemy.sql.functions import user
from werkzeug.security import check_password_hash


@auth.route('/login1')
def login1():
    return render_template('login1.html')
#Added part
@auth.route('/login1',methods=['POST'])
def login1_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember')else False

    from gunicorn.config import User
    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password,hash it and compare it to the hash  password in the database
    if not user or not check_password_hash(user.password,password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong,reload the page
    # if the above check passes,the know the user has the right credentials
    return redirect(url_for('main.py.profile'))


@auth.route('/signup1', method=['POST'])
def signup1_post():
    return render_template('signup1.html')


@auth.route('/signup1', methods=['POST'])
def signup1_post():
    if user:  # if a user is found,we want to redirect back to signup page so user can try again.
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

@auth.route('/login1')
def login1():
    return render_template('login1.html')

@auth.route('/signup1')
def signup1():
    return render_template('signup1.html')
