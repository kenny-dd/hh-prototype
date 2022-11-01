from urllib.error import URLError
from app import app

from flask import render_template, request, redirect, abort

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

# Risk Select
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

# Volunteer Select
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

# Organization Representative
@app.route("/org_rep")
def rep_org():
    return render_template("public/org_rep.html")

# Search Results
@app.route("/search_results")
def search_results():

    organizations = {
        "Addiction Resource 1"
    }

    services = [
        "Counseling",
        "Addiction Programs",
        "Psychological Services",
        "Food",
        "Available Today: 7am-7pm"
    ]
    return render_template("public/search_results.html", organizations=organizations, services=services)

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

# Log into Account
@app.route("/login")
def login():
    return render_template("public/login.html")

# Help Me Page
@app.route("/help_me")
def help_me():
    return render_template("public/help_me.html")

# User Profile Page
@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template("public/profile.html", user=user, username=username)

@app.route("/jinja")
def jinja():

    my_name = "Kenny"

    age = 21

    langs = ["Python", "JavaScript", "Bash", "C"]

    friends = {
        "Tom": "30",
        "Amy": 60,
        "Tony": 24,
        "Clarissa": 24
    }

    colors = {"Red", "Green"}

    cool = True

    class gitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
                return f"Pulling repo {self.name}"

        def clone(self):
                return f"Cloning into {self.url}"

    my_remote = gitRemote(
        name="Flask Jinja",
        description="Template Design Tutorial",
        url="https://github.com/kenny-dd"
    )

    def repeat(x, qty):
        return x * qty

    return render_template("public/jinja.html", my_name=my_name, age=age, langs=langs, 
    friends=friends, colors=colors, cool=cool, gitRemote=gitRemote, repeat=repeat, my_remote=my_remote)
