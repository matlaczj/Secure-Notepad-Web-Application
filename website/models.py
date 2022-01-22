from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func, expression

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    isPublic = db.Column(db.Boolean, server_default=expression.false(), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    owner_email = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
