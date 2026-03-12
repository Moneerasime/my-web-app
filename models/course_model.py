from models.user_model import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    instructor = db.Column(db.String(100))