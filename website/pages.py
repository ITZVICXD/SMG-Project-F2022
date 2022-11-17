from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, db


pages = Blueprint('pages', __name__)

@pages.route("/")
def com():
    return redirect(url_for('pages.home'))

@pages.route("/Home")
#@login_required
def home():
    return render_template("home.HTML", user=current_user)

@pages.route("/Calendar")
def calendar():
    return render_template("syncCalendar.HTML")

@pages.route("/Profile")#In order to use must url must be /Home/profile?name=EnterNameHere
def profile():
    return render_template("profile.HTML")
@pages.route("/Transcript Reader")
def TR():
    return render_template("TR.HTML", user=current_user)
