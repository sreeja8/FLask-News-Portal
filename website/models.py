from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model): #schema of Note
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    ##Foreign Key relationship - mapping note to the user -- one to many relationship -- user -> notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #users = db.relationship('User')

class User(db.Model, UserMixin): #schema of Users
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note', backref='user')