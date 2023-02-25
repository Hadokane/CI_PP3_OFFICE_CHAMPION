from flask import (
    Flask, render_template, url_for, request,
    redirect, session, flash)
from officechampion import app, db
# imports tables from models document
from officechampion.models import User, Note, League, Title
# stores the saved password as a secure hash
from werkzeug.security import generate_password_hash, check_password_hash
# flask user files to handle login/out requests and data
from flask_login import login_user, login_required, logout_user, current_user


# returns the homepage when Flask is ran
# app route decorator uses "/"" to send user to homepage
@app.route("/")
def home():
    return render_template("index.html", user=current_user)


# displays the notes page, requires login to view
# giving it note functionality to see if user can store data
@app.route("/notes", methods=["GET", "POST"])
@login_required
def notes():
    if request.method == "POST":
        note = request.form.get("note")
        # ensure something is written in the note
        if len(note) < 3:
            flash("Note is too short!", category="error")
        # checks user id & POSTs the note
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")
    return render_template("notes.html", user=current_user)


# Edit notes, use notes id to generate route
@app.route("/edit_notes/<int:note_id>", methods=["GET", "POST"])
@login_required
def edit_notes(note_id):
    # Get note name from the form or trigger 404 error
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.data = request.form.get("data")
        note.date = request.form.get("date")
        db.session.commit()
        flash("Note updated!", category="success")
        return redirect(url_for("notes"))
    return render_template(
        "edit_notes.html", user=current_user, note=note)


# Delete a note
@app.route("/delete_note/<int:note_id>")
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    flash("Note deleted!", category="success")
    return redirect(url_for("notes"))


# displays the sign-up page
@app.route("/sign_up", methods=["GET", "POST"])
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
            # logs in the user by finding there name first
            user = User.query.filter_by(username=username).first()
            login_user(user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("home"))
    return render_template("sign_up.html", user=current_user)


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
                flash("Login Successful", category="success")
                # remembers user is logged in, unless cache cleared
                login_user(user, remember=True)
                return redirect(url_for("home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Username does not exists.", category="success")
    # flash("Login Successful!", category="success")
    return render_template("login.html", user=current_user)


# logs the user out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# Add the league page
@app.route("/league")
@login_required
def league():
    # Reads db and orders all data by league name values
    league = list(League.query.order_by(League.league_name).all())
    return render_template(
        "league.html", user=current_user, league=league)


# Add a league
@app.route("/add_league", methods=["GET", "POST"])
@login_required
def add_league():
    if request.method == "POST":
        # Get league name from the form
        new_league = League(
            league_name=request.form.get("league_name"),
            user_id=current_user.id)
        # Add it to the table
        db.session.add(new_league)
        db.session.commit()
        # Provide positive user feedback
        flash("League Added!", category="success")
        # Redirect back to the league page
        return redirect(url_for("league"))
    return render_template("add_league.html", user=current_user)


# Edit a league, use leagues id to generate route
@app.route("/edit_league/<int:league_id>", methods=["GET", "POST"])
@login_required
def edit_league(league_id):
    # Get league name from the form or trigger 404 error
    league = League.query.get_or_404(league_id)
    if request.method == "POST":
        league.league_name = request.form.get("league_name")
        db.session.commit()
        return redirect(url_for("league"))
    return render_template(
        "edit_league.html", user=current_user, league=league)


# Delete a league
# set modals id to match the league_id
@app.route("/delete_league/<int:league_id>")
@login_required
def delete_league(league_id):
    league = League.query.get_or_404(league_id)
    db.session.delete(league)
    db.session.commit()
    return redirect(url_for("league"))


# Link to titles page
@app.route("/titles")
@login_required
def titles():
    # Reads db and orders all data by league name values
    titles = list(Title.query.order_by(Title.title_name).all())
    return render_template("titles.html", user=current_user, titles=titles)


# Add a title
@app.route("/add_titles", methods=["GET", "POST"])
@login_required
def add_titles():
    # Reads db and orders all data by league name values
    user = list(User.query.order_by(User.username).all())
    league = list(League.query.order_by(League.league_name).all())
    if request.method == "POST":
        new_title = Title(
            title_name=request.form.get("title_name"),
            title_description=request.form.get("title_description"),
            champion_since=request.form.get("champion_since"),
            image_url=request.form.get("image_url"),
            league_id=request.form.get("league_id"),
            user_id=current_user.id
        )
        # Add it to the table
        db.session.add(new_title)
        db.session.commit()
        # Provide positive user feedback
        flash("Title Added!", category="success")
        # Redirect back to the league page
        return redirect(url_for("titles"))
    return render_template("add_titles.html", user=current_user, league=league)
