from flask import (
    Flask, render_template, url_for, request, redirect, session, flash)
from officechampion import app, db
# imports tables from models document
from officechampion.models import User, Note
# stores the saved password as a secure hash
from werkzeug.security import generate_password_hash, check_password_hash
# flask user files to handle login/out requests and data
from flask_login import login_user, login_required, logout_user, current_user


# returns the homepage when Flask is ran
# app route decorator uses "/"" to send user to homepage
@app.route("/")
def home():
    return render_template("index.html", value="Uno")


# displays the test page, requires login to view
@app.route("/test")
@login_required
def test():
    return render_template("test.html", value="Deux")


# displays the sign-up page
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # when data is POSTed we acquire the requested information
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        # checks to see if user already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already in use.", category="error")
        # if username is shorter than 4 characters
        elif len(username) < 4:
            flash(
                "Username must be greater than 3 characters.",
                category="error")
        # if username is longer than 25 characters
        # maxlength allowed
        elif len(username) > 25:
            flash(
                "Username cannot exceed 25 characters.",
                category="error")
        # if password is shorter than 7 characters
        elif len(password1) < 8:
            flash(
                "Password must be greater than 7 characters.",
                category="error")
        # if password is longer than 25 characters
        # maxlength allowed
        elif len(password1) > 25:
            flash(
                "Password cannot exceed 25 characters.",
                category="error")
        # if password's dont match
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        # adds the new user to database
        # hashes password for security using sha256 method
        else:
            new_user = User(
                username=username, password=generate_password_hash(
                    password1, method="sha256")
                )
            # saves the information to User table
            db.session.add(new_user)
            db.session.commit()
            # logs in the user
            login_user(user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("home"))
    return render_template("sign_up.html")


# handles login data requests
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # searches the User table and compares username entered
        # against those stored within the db
        # should only be 1 result, as unique usernames so check first result
        user = User.query.filter_by(username=username).first()
        # if username exists, compare the password against hashed result
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successful!y", category="success")
                # remembers user is logged in, unless cache cleared
                login_user(user, remember=True)
                return redirect(url_for("home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Username does not exists.", category="success")
    # flash("Login Successful!", category="success")
    return render_template("login.html")


# logs the user out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
