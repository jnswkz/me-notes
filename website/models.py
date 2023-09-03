from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note (db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key is a unique identifier for each note
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user_id is a foreign key that references the id column of the user table


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key is a unique identifier for each user
    username = db.Column(db.String(150), unique=True) # unique=True means that no two users can have the same username
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship('Note') # this is a relationship between the user and the note table


    