from . import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # hashed
    role = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(100), nullable=True)
