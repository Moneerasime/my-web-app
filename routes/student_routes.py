from flask import Blueprint, render_template

student_bp = Blueprint("student", __name__, url_prefix="/student")

@student_bp.route("/dashboard")
def dashboard():
    return render_template("student/dashboard.html")

@student_bp.route("/courses")
def courses():
    return render_template("student/courses.html")

@student_bp.route("/grades")
def grades():
    return render_template("student/grades.html")

@student_bp.route("/attendance")
def attendance():
    return render_template("student/attendance.html")