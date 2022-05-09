from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app import app


def create_app(models=None):
    db.init_app(app)
    login_manager = LoginManager
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))