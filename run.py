import os
from flask import Flask, render_template, url_for, request, redirect

# set Flask equal to app
app = Flask(__name__)


# returns the homepage when Flask is ran
# app route decorator uses "/"" to send user to homepage
# adding the username variable as a placeholder, displays on html page
@app.route("/")
def home():
    return render_template("index.html", username="username")


# displays the test page
# changes the username to steven for test purposes
@app.route("/test")
def test():
    return render_template("test.html", username="steven")


# handles data requests
@app.route("/login", methods=["GET", "POST"])
def login():
    # when data is posted to us via the form, the name field is read
    # user is then directed to a new page using their name as a value
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    # no data currently returns user home as nothing is amended to the url
    else:
        return render_template("login.html")


# uses the name read by the above login request to display it on a new page
@app.route("/<usr>")
def user(usr):
    return f"<h1>Hello {usr}!</h1>"


# debug allows the app to reload without relaunching every change
# set to false before publishing
# runs an instance of Flask
if __name__ == "__main__":
    app.run(debug=True)
