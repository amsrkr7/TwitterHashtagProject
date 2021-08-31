from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin


db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    screen_name = db.Column(db.String(256), unique=True)
    name = db.Column(db.String(256))
    description = db.Column(db.String(256))
    geo_enabled = db.Column(db.Boolean)
    location = db.Column(db.String(256))
    img = db.Column(db.String(255))
    #friends = db.Column(db.Integer)
    #statuses = db.Column(db.Integer)
    #tweets = db.relationship('Tweet', back_populates='user')


class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)

class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(primary_key=True)
    text = db.Column(db.String(320))
    #created_time = db.Column(db.DateTime)
    #retweets = db.Column(db.Integer)
    #user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    #user = db.relationship('User', back_populates='tweets')

class Trending(db.Model):
    __tablename__ = 'trends'
    trend = db.Column(db.String(), primary_key=True)
    url = db.Column(db.String(320))
    query = db.Column(db.String(320))
    tweet_volume = db.Column(db.Integer)

# setup login manager
login_manager = LoginManager()
login_manager.login_view = 'twitter.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))