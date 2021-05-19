from datetime import datetime
from flask_login import UserMixin, LoginManager
from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from database import db
from werkzeug.security import generate_password_hash, check_password_hash

def is_username_available(username):
    existing_user = user_with_username(username)
    return (existing_user is None)

def user_with_username(username):
    return db.session.query(User).filter_by(username=username).first()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128))
    admin_role = db.Column(db.Boolean, default=False, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.fromtimestamp(0))
    avatar = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
