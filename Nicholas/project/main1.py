from flask import Blueprint,render_template
from flask_login import login_required,current_user
from.import db
from pymongo import auth

from pythonProject import main
from.import db

@main.route('/')
def index():
    return render_template('index1.html')

@main.route('/profile')
def profile():
    return render_template('profile1.html')
