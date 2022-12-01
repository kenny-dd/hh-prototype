from urllib.error import URLError
from app import app

from flask import Flask, render_template, request, redirect, abort, flash, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired

# app = Flask(__name__)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# Home Page
@app.route("/")
def index():
    return render_template("public/index.html")

# About Us Page
@app.route("/about")
def about():
    return render_template("public/about.html")

# Resources Page
@app.route("/resources")
def resources():

    addiction = [
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma",
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma",
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma",
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma"
    ]

    health = [
        "https://www.wm.edu/offices/wellness/healthcenter/",
        'https://www.wm.edu/offices/wellness/healthcenter/',
        'https://www.wm.edu/offices/wellness/healthcenter/',
        'https://www.wm.edu/offices/wellness/healthcenter/'
    ]

    mentalHealth = [
        'https://www.mentalhealthfirstaid.org/mental-health-resources/',
        'https://www.mentalhealthfirstaid.org/mental-health-resources/',
        'https://www.mentalhealthfirstaid.org/mental-health-resources/',
        'https://www.mentalhealthfirstaid.org/mental-health-resources/'
    ]

    return render_template("public/resources.html", addiction=addiction, health=health, mentalHealth=mentalHealth)

# Contact Page
@app.route("/contact")
def contact():
    return render_template("public/contact.html")

# Risk Select Form
@app.route("/risk_select")
def risk_select():
    selectList = [
        ['food', 'Food'],
        ['shelter', 'Shelter'],
        ['medicine', 'Medicine'],
        ['mentalHealth', 'Mental Health'],
        ['addiction', 'Addiction'],
    ]
    return render_template("public/risk_select.html", selectList=selectList)

# Volunteer Select Form
@app.route("/volunteer_select")
def volunteer_select():

    selectList = [
        ['food', 'Food'],
        ['shelter', 'Shelter'],
        ['medicine', 'Medicine'],
        ['mentalHealth', 'Mental Health'],
        ['addiction', 'Addiction'],
    ]

    return render_template("public/volunteer_select.html", selectList=selectList)

# Search Results Page
@app.route("/search_results")
def search_results():

    organizations = [
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma",
        "https://www.wm.edu/offices/wellness/healthcenter/",
        'https://www.mentalhealthfirstaid.org/mental-health-resources/',
    ]

    localities = [
        "123 fictional Food and Counseling 1 lane, Norfolk VA 23508",
        "123 fictional Food 1 lane, Norfolk VA 23508",
        "123 fictional shelter 3 lane, Norfolk VA 23508",
    ]

    programs = [
        "Counseling",
        "Addiction",
        "Psychological Services",
        "Blood Donation"
    ]

    return render_template("public/search_results.html", organizations=organizations, localities=localities, programs=programs)

# Register for an Account
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        req = request.form

        org_name = req.get("org_name")
        username = req.get("username")
        first_name = req.get("first_name")
        last_name = req.get("last_name")
        email = req.get("email")
        password = req.get("password")

        print(username, first_name, last_name, email, password)

        return redirect(request.url)

    return render_template("public/register.html")

users = {
    "kenny": {
        "name": "Kenny Dang",
        "bio": "Creation of Kenny",
        "twitter": "@ynnekd"
    },
     "mark": {
        "name": "mark twain",
        "bio": "Creation of Pool Noodles",
        "twitter": "@mtwain"
    },
     "lester": {
        "name": "lester park",
        "bio": "Tester Test",
        "twitter": "@lesterp"
    }
}

# Login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Log into Account
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("public/login.html", form=form)

# Log out of Account
@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for('/login'))

# Help Me Page
@app.route("/help_me")
def help_me():
    return render_template("public/help_me.html")

# User Profile Page
@app.route("/profile")
def profile():
    return render_template("public/profile.html")

# Organization Resource Page
@app.route("/org_resource")
def org_resource():

    services = [
        "Counseling",
        "Addiction Programs",
        "Psychological Services",
        "Food",
        "Available Today: 7am-7pm"
    ]
    
    return render_template("public/org_resource_page.html", services=services)

# Program Resource Page
@app.route("/prog_resource")
def program_resource():
    return render_template("public/prog_resource_page.html")

# Locality Resource Page
@app.route("/loc_resource")
def locality_resource():
    return render_template("public/loc_resource_page.html")