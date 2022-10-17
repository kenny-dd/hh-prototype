from urllib.error import URLError
from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/resources")
def resources():

    resources = [
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma",
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma",
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma",
        "https://www.samhsa.gov/homelessness-programs-resources/hpr-resources/trauma"
    ]

    return render_template("public/resources.html", resources=resources)

@app.route("/contact")
def contact():
    return render_template("public/contact.html")

@app.route("/risk_select")
def risk_select():
    return render_template("public/content/risk_select.html")

@app.route("/volunteer_select")
def volunteer_select():
    return render_template("public/content/volunteer_select.html")

@app.route("/org_rep")
def rep_org():
    return render_template("public/content/org_rep.html")

@app.route("/search_results")
def search_results():

    organizations = {
        "Organization Services"
    }

    services = [
        "Counseling",
        "Addiction Programs",
        "Psychological Services",
        "Food",
        "Available Today: 7am-7pm"
    ]

    return render_template("public/search_results.html", organizations=organizations, services=services)

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