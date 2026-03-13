from flask import Blueprint, render_template, request, redirect, session
from models.user_model import db, User

auth_bp = Blueprint("auth", __name__)

# الصفحة الرئيسية
@auth_bp.route("/")
def main():
    return render_template("main.html")


# صفحة تسجيل الدخول
@auth_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        # البحث عن المستخدم بالبريد فقط
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:

            session["name"] = user.name
            session["role"] = user.role

            # توجيه المستخدم حسب الدور
            if user.role == "طالب":
                return redirect("/student/dashboard")
            elif user.role == "دكتور":
                return redirect("/faculty/dashboard")
            elif user.role == "إدارة":
                return redirect("/admin/dashboard")

        return "⚠️ البريد الإلكتروني أو كلمة المرور غير صحيحة"

    return render_template("login.html")

@auth_bp.route("/register")
def register():
    return render_template("register.html")

@auth_bp.route("/create_user", methods=["POST"])
def create_user():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    role = request.form["role"]
    department = request.form["department"]
    student_id = request.form["student_id"]
    phone = request.form["phone"]

    # التحقق من البريد الإلكتروني
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return "⚠️ البريد الإلكتروني مستخدم مسبقاً"

    # التحقق من الرقم الجامعي
    existing_student = User.query.filter_by(student_id=student_id).first()
    if existing_student:
        return "⚠️ الرقم الجامعي مسجل مسبقاً"

    # التحقق من رقم الهاتف
    existing_phone = User.query.filter_by(phone=phone).first()
    if existing_phone:
        return "⚠️ رقم الهاتف مستخدم مسبقاً"

    # إنشاء المستخدم
    new_user = User(
        name=name,
        email=email,
        password=password,
        role=role,
        department=department,
        student_id=student_id,
        phone=phone
    )

    db.session.add(new_user)
    db.session.commit()

    # تسجيل دخول المستخدم مباشرة بعد إنشاء الحساب
    session["name"] = new_user.name
    session["role"] = new_user.role

    # تحويل المستخدم حسب الدور
    if new_user.role == "طالب":
        return redirect("/student/dashboard")
    elif new_user.role == "دكتور":
        return redirect("/faculty/dashboard")
    elif new_user.role == "إدارة":
        return redirect("/admin/dashboard")

    # fallback
    return redirect("/login")


@auth_bp.route("/create_faculty", methods=["POST"])
def create_faculty():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    phone = request.form.get("phone")

    faculty_id = request.form.get("faculty_id")
    department = request.form.get("department")
    college = request.form.get("college")

    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    role = request.form.get("role")

    # التحقق من تطابق كلمة المرور
    if password != confirm_password:
        return "⚠️ كلمة المرور غير متطابقة"

    # التحقق من البريد الإلكتروني
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return "⚠️ البريد الإلكتروني مستخدم بالفعل"

    # إنشاء الاسم الكامل
    full_name = first_name + " " + last_name

    new_user = User(
        name=full_name,
        email=email,
        password=password,
        role=role,
        department=department,
        phone=phone,
        student_id=faculty_id
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect("/login")

# صفحة نسيت كلمة المرور
@auth_bp.route("/forgot_password")
def forgot_password():
    return render_template("forgot_password.html", previous_page="/login")

# تغيير كلمة المرور
@auth_bp.route("/reset_password", methods=["POST"])
def reset_password():

    email = request.form["email"]
    new_password = request.form["new_password"]

    user = User.query.filter_by(email=email).first()

    if user:
        user.password = new_password
        db.session.commit()
        return redirect("/login")

    return "البريد الإلكتروني غير موجود"

# صفحة اختيار نوع الحساب
@auth_bp.route("/select_account_type")
def select_account_type():
    return render_template("select_account_type.html", previous_page="/login")

# صفحة تسجيل الطالب
@auth_bp.route("/register_student")
def register_student():
    return render_template("register_student.html", previous_page="/select_account_type")
# صفحة تسجيل الدكتور
@auth_bp.route("/register_faculty")
def register_faculty():
    return render_template("register_faculty.html", previous_page="/select_account_type")
