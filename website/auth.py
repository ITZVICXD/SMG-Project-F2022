from flask import Blueprint, render_template, request, flash, redirect, url_for, g, session
from .models import User, db
from website import app
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("Login.HTML")
@auth.route('/logout')
def logout():
     return redirect(url_for('pages.home'))
     
@auth.route('/Register', methods=['GET', 'POST'])
def Register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #user = User.query.filter_by(email=email).first()

        if len(first_name) <= 3:
            flash('A First Name is Required', category='error')
        elif len(last_name) <= 2:
            flash('A Last Name is Required', category='error')
        elif len(email) <= 2:
            flash('A Email is Required', category='error')
        elif len(password1) <= 7:
            flash('A Password is Required', category='error')
        elif password1 != password2:
            flash('Passwords Do Not Match', category='error')
        else:
            #add user to the database
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password2, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #users = db.session.execute(db.select(User)).scalars()
            flash('Account Created', category='success')
            return redirect(url_for('pages.home'))
            


    return render_template("register.HTML")