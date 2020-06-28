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