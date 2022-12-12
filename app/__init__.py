from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY']="TeamGreen2022"

from app import views

from app import admin_views

from app import error_handlers