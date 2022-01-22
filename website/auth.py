from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from helpers.password_policy import getPasswordStrengthScore
import time

auth = Blueprint('auth', __name__)

from helpers import nLoginTrialsInLastHourForEmail,ipAddressesForEmail

@auth.route('/login', methods=['GET', 'POST'])
def login():
    global nLoginTrialsInLastHourForEmail,ipAddressesForEmail
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #time.sleep(3)
        remote_addr = request.remote_addr
        ipAddressesForEmail[email].append(remote_addr)
        ipAddressesForEmail[email] = list(set(ipAddressesForEmail[email]))
        if(len(ipAddressesForEmail[email]) > 1):
            flash('Someone else might have taken control over your account.', category='error')
        print(f"ipAddressesForEmail={ipAddressesForEmail}")

        if(nLoginTrialsInLastHourForEmail[email] > 3):
            flash('You tried wrong password too many times. Wait an hour.', category='error')
            return render_template("login.html", user=current_user)

        nLoginTrialsInLastHourForEmail[email] += 1
        trialsLeft = 4 - nLoginTrialsInLastHourForEmail[email]
        print(nLoginTrialsInLastHourForEmail)

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                nLoginTrialsInLastHourForEmail[email] = 0
                return redirect(url_for('views.home'))
            else:
                flash(f'Incorrect password, try again. You have {trialsLeft} trials left.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        passwordStrengthScore = getPasswordStrengthScore(password1)
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) <= 2:
            flash('Email must be greater than 2 characters.', category='error')
        elif len(first_name) <= 1:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif(passwordStrengthScore < 0.66):
            flash(f'Password is too weak with strenght = {passwordStrengthScore*100}%', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='pbkdf2:sha256:1000000',salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
