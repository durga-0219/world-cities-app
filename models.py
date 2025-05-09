from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    cities = db.relationship('City', backref='country')

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    population = db.Column(db.Integer)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
