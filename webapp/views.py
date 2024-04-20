from flask import *
import os

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/ce441")
def home():
    return render_template("exp.html")

@views.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join("webapp",'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
