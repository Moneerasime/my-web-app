from models.user_model import db

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(100))
    course = db.Column(db.String(100))
    grade = db.Column(db.String(10))