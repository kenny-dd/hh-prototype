from app import app

from flask import render_template, request

# 404 Error Page
@app.errorhandler(404)
def not_found(e):
    return render_template('/public/404.html')
    