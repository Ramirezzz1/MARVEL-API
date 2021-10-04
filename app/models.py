from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime
import uuid

from werkzeug.security import generate_password_hash

login= LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db = SQLAlchemy()

class Avenger(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    hero = db.Column(db.String(150), nullable=False, unique=True)
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    age = db.Column(db.Integer)
    hometown= db.Column(db.String(150))
    powers = db.Column(db.String(150))
    weaknesses = db.Column(db.String(150))

    def roster(self):
        return {
            'id': self.id,
            'hero': self.hero,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'age':self.age,
            'hometown':self.hometown,
            'powers':self.powers,
            'weaknesses':self.weaknesses
            

        }

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, default='')
    password = db.Column(db.String(32), nullable=False)
    first_name= db.Column(db.String(150), nullable= True, default='')
    last_name=db.Column(db.String(150), nullable=True, default='')
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.password = generate_password_hash(password)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid.uuid4())


    def to_dict(self):
        return {
            'id': self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'username': self.username,
            'email':self.email,
            'date_created': self.date_created
        }


