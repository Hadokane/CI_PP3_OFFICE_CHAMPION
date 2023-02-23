from flask import (
    Flask, render_template, url_for, request, redirect, session, flash)
from datetime import timedelta
from officechampion import app, db

# stores session data on browser for 5 days
app.permanent_session_lifetime = timedelta(days=5)


# returns the homepage when Flask is ran
# app route decorator uses "/"" to send user to homepage
# adding the username variable as a placeholder, displays on html page
@app.route("/")
def home():
    return render_template("index.html", value="Uno")


# displays the test page
# changes the username to steven for test purposes
@app.route("/test")
def test():
    return render_template("test.html", value="Deux")


# handles data requests
@app.route("/login", methods=["GET", "POST"])
def login():
    # when data is posted to us via the form, the name field is read
    # user is then directed to a new page using their name as a value
    if request.method == "POST":
        # makes this session last as long as defined on line 10 of this doc
        session.permanent = True
        user = request.form["name"]
        # session stores data in a dictionary while the user is on the site
        session["user"] = user
        return redirect(url_for("user"))
        flash("Login Successful!")
    # no data currently returns user home as nothing is amended to the url
    else:
        if "user" in session:
            # flashes a message to provide user action feedback
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")


# uses the name read by the above login request to display it on a new page
@app.route("/user")
def user():
    # if someone has logged in on the login form, session reads the username
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    # if not logged in, sends the user to the login form
    else:
        # flashes a message to provide user action feedback
        flash("You are not logged in!")
        return render_template("login.html")


# logs the user out of their session
@app.route("/logout")
def logout():
    if "user" in session:
        # alerts user they have signed out
        flash("You have been logged out!", "info")
    else:
        # alerts a non-signed in user that they aren't logged in
        flash("You are not logged in!")

    session.pop("user", None)
    return redirect(url_for("login"))


# displays the test page
# changes the username to steven for test purposes
@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html", value="Deux")
