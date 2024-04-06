
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(128), unique = True)
    username = db.Column(db.String(128), unique = True)
    phone = db.Column(db.String(128))
    country = db.Column(db.String(100))


def seed_data():
    faker = Faker()
    while User.query.count() < 100:
        new_name = faker.name()
        new_age = random.randint(20, 80)
        new_email = faker.email()
        new_username = faker.user_name()
        new_phone = str(random.randint(10000000,99999999))
        new_country = faker.country() 
        
        new_user = User(name=new_name, age=new_age,email=new_email, username=new_username, phone=new_phone, country=new_country)
        db.session.add(new_user)
        db.session.commit()
