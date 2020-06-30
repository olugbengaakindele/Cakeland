from app import db
from datetime import datetime


class Visits(db.Model):
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    visit_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, count , visit_date):
        self.count = count
        self.visit_date = visit_date



class Pictures(db.Model):
    __tablename__ = 'pictures'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(100))
    category= db.Column(db.String(100))
    description = db.Column(db.String(100))
    price = db.Column(db.Integer)
    add_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, count , file_name,description, price, visit_date):

        self.file_name = file_name 
        self.category= category
        self.description = description
        self.price= price
        self.visit_date = visit_date

    
    def __repr__(self):
        return "File has been added to database"