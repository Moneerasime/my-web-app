from flask import Blueprint, render_template

faculty_bp = Blueprint("faculty", __name__, url_prefix="/faculty")

@faculty_bp.route("/dashboard")
def dashboard():
    return render_template("faculty/dashboard.html")

@faculty_bp.route("/courses")
def courses():
    return render_template("faculty/manage_courses.html")

@faculty_bp.route("/grades")
def grades():
    return render_template("faculty/enter_grades.html")