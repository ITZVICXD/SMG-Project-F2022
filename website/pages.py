from flask import Blueprint, render_template, request

pages = Blueprint('pages', __name__)

@pages.route("/Home")
def home():
    return render_template("home.HTML")

@pages.route("/Profile")#In order to use must url must be /Home/profile?name=EnterNameHere
def profile():
    args = request.args
    name = args.get('name')
    return render_template("profile.HTML", name=name)
