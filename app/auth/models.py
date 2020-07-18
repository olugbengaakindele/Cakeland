from app import db, bcrypt
from datetime import datetime
from app import loginmanager
from flask_login import UserMixin




class Visits(db.Model):
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    visit_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, count, visit_date):
        self.count = count
        self.visit_date = visit_date


class Pictures(db.Model):
    __tablename__ = 'pictures'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    description = db.Column(db.String(100))
    price = db.Column(db.Integer)
    add_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, count, file_name,category, description, price, visit_date):
        self.file_name = file_name
        self.category = category
        self.description = description
        self.price = price
        self.visit_date = visit_date

    def __repr__(self):
        return "File has been added to database"


class User(UserMixin,db.Model ):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))
    reg_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return 'Account created'

    @classmethod
    def create_user(cls, username, password, role):
        user = cls(username=username,
                   password=bcrypt.generate_password_hash(password).decode('utf-8'),
                   role=role)

        db.session.add(user)
        db.session.commit()

        return user


@loginmanager.user_loader
def load_user(id):
    return User.query.get(int(id))