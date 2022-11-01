from app import app

from flask import render_template

# Admin Dashboard
@app.route("/admin/dashboard")
def dashboard():
    return render_template("/admin/dashboard.html")

# Admin Profile
@app.route("/admin/profile")
def admin():
    return render_template("/admin/profile.html")