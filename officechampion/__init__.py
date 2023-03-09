import os
from flask import (
    Flask, url_for, redirect, flash)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

if os.path.exists("env.py"):
    import env  # noqa


# set Flask equal to app variable
app = Flask(__name__)
# allows us to read encrypted data (eg - sessions)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":  # local
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:  # elephantSQL
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)
admin = Admin(app)
login = LoginManager(app)


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


# Custom ModelView to add security
# ID==3 is Username: Admin
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.id == 3

    # If another user goes directly to a url like /admin/user
    # This redirects them to the home screen
    def inaccessible_callback(self, name, **kwargs):
        flash("You are not the Admin!", category="warning")
        return redirect(url_for("home"))


# Add administrative views here
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(League, db.session))
admin.add_view(MyModelView(Member, db.session))
admin.add_view(MyModelView(Note, db.session))
admin.add_view(MyModelView(Title, db.session))
