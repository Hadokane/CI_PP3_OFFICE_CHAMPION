import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

# set Flask equal to app variable
app = Flask(__name__)
# allows us to read encrypted data (eg - sessions)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local

db = SQLAlchemy(app)


# reliant on the above Flask app & db already running
# so placed at bottom of this document
from officechampion import routes  # noqa
