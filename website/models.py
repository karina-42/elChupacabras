from . import db
from flask_login import UserMixin
# from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    """
    Represents a registered user in the app

    Attributes:
        id (int): The user's unique ID number. Primary key
        email (str): The user's unique email
        username (str): The user's unique username
        password (str): The user's hashed password
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


# TODO: add something to store the record time, time = Column whatever
# class TimeRecord(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
