from app import db


class Pet(db.Model):
    id = db.Collumn(db.Integer, primary_key = True)
    name = db.Collumn(db.String)
    age = db.Collumn(db.Integer)
    owner = db.Collumn(db.String)
    breed = db.Collumn(db.String)
    

