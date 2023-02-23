from flask import (
    Flask, render_template, url_for, request, redirect, session, flash)
from datetime import timedelta
from officechampion import app, db

# stores session data on browser for 5 days
app.permanent_session_lifetime = timedelta(days=5)


# returns the homepage when Flask is ran
# app route decorator uses "/"" to send user to homepage
@app.route("/")
def home():
    return render_template("index.html", value="Uno")


# displays the test page
@app.route("/test")
def test():
    return render_template("test.html", value="Deux")


# handles login data requests
@app.route("/login", methods=["GET", "POST"])
def login():
    # gets the data from the POST request of the form
    data = request.form
    # prints it to the console
    print(data)
    # flash("Login Successful!", category="success")
    return render_template("login.html")


# logs the user out of their session
@app.route("/logout")
def logout():
    return "<p>Logout</p>"


# displays the sign-up page
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # when data is POSTed we acquire the requested information
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        # if username is shorter than 4 characters
        if len(username) < 4:
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
        # add user to database
        else:
            flash("Account created!", category="success")

    return render_template("sign_up.html")
