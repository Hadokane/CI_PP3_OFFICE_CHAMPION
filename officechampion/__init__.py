import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
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
from officechampion.models import User, Note, League, Title, Member  # noqa


# tells flask login manager how to load a user
login_manager = LoginManager()
login_manager.login_view = 'home'
login_manager.init_app(app)


# tells flask to reference the user by id
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
