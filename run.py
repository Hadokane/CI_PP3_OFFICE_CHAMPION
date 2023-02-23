import os
from flask import Flask

# set Flask equal to app
app = Flask(__name__)


# returns the homepage when Flask is ran
# app route decorator uses "/"" to send user to homepage
@app.route("/")
def home():
    return "<h1>Hello! This is working.</h1><p>good job!</p>"


# runs an instance of Flask
if __name__ == "__main__":
    app.run()
