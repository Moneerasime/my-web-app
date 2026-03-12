from models.user_model import db

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(100))
    course = db.Column(db.String(100))
    status = db.Column(db.String(20))