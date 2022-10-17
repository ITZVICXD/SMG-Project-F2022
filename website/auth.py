from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("Login.HTML")
@auth.route('/logout')
def logout():
    return render_template("Logout.HTML")
@auth.route('/Register')
def Register():
    return render_template("register.HTML")