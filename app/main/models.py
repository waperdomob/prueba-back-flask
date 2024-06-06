from datetime import datetime

from app.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
        }

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date_created': self.date_created,
            'user_id': self.user_id
        }
