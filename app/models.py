from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Avenger(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    hero = db.Column(db.String(100), nullable=False, unique=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    age = db.Column(db.Integer)
    hometown= db.Column(db.String(100))
    powers = db.Column(db.String(100))
    weaknesses = db.Column(db.String(100))

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