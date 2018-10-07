# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The models module from the app database."""

from datetime import datetime
from flask_login import UserMixin
from . import db, lm


class Twitt(db.Model):
    __tablename__ = 'twitts'
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Twitt ({self.id}) {self.text}>'

    @property
    def url(self):
        query = db.session.query(User.username)
        query = query.filter_by(id=self.user_id)
        username, = query.first()
        return f'https://twitter.com/{username}/status/{self.id}'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    access_token_key = db.Column(db.String(64), nullable=True)
    access_token_secret = db.Column(db.String(64), nullable=True)
    twitts = db.relationship('Twitt', backref='user')

    def __repr__(self):
        return f'<User ({self.id}) {self.username}>'

    def get_access_token(self):
        return (self.access_token_key, self.access_token_secret)

    def set_access_token(self, token):
        self.access_token_key = token[0]
        self.access_token_secret = token[1]


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
