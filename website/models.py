from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    """
    Represents a registered user in the app

    Attributes:
        id (int): The user's unique ID number. Primary key
        email (str): The user's unique email
        username (str): The user's unique username
        password (str): The user's hashed password
        records (list): The time records associated with this user
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    records = db.relationship('TimeRecord')


class TimeRecord(db.Model):
    """
    Represents the time it took for the player to successfully complete the
    game

    Attributes:
        id (int): The time record's unique ID number. Primary key
        user_id (int): The user id tied to this record. Foreign key
        date (datetime): The date and time the user recorded this record
        elapsed_time (float): The time calculated that the user spent to
            complete the game successfully

    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    elapsed_time = db.Column(db.Float)
