from flask import *
import os

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
