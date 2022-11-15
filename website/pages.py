from flask import Blueprint, render_template, request

pages = Blueprint('pages', __name__)

@pages.route("/Home")
def home():
    return render_template("home.HTML")

@pages.route("/Calendar")
def calendar():
    return render_template("syncCalendar.HTML")

@pages.route("/Profile")#In order to use must url must be /Home/profile?name=EnterNameHere
def profile():
    return render_template("profile.HTML")
