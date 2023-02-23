import os
from flask import Flask, render_template, url_for

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


# debug allows the app to reload without relaunching every change
# set to false before publishing
# runs an instance of Flask
if __name__ == "__main__":
    app.run(debug=True)
