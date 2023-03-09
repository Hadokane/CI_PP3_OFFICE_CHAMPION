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
class UserView(ModelView):
    can_create = False  # disable model deletion
    can_edit = False  # disable model deletion
    can_delete = False  # disable model deletion
    can_export = True  # allows export of data as a spreadsheet
    page_size = 25  # the number of entries to display on the list view
    column_list = ('id', 'username')
    column_searchable_list = ['id', 'username']

    def is_accessible(self):
        return current_user.id == 3


# Custom ModelView
class LeagueView(ModelView):
    can_create = False  # disable model deletion
    can_edit = False  # disable model deletion
    can_delete = False  # disable model deletion
    can_export = True  # allows export of data as a spreadsheet
    page_size = 25  # the number of entries to display on the list view
    column_list = (
        'user_id', 'league_name')
    column_searchable_list = [
        'user_id', 'league_name']

    def is_accessible(self):
        return current_user.id == 3


# Custom ModelView
class TitleView(ModelView):
    can_create = False  # disable model deletion
    can_edit = False  # disable model deletion
    can_delete = False  # disable model deletion
    can_export = True  # allows export of data as a spreadsheet
    page_size = 25  # the number of entries to display on the list view
    column_list = (
        'user_id', 'title_name', 'title_description', 'league.league_name')
    column_searchable_list = [
        'user_id', 'title_name', 'title_description', 'league.league_name']

    def is_accessible(self):
        return current_user.id == 3


# Custom ModelView
class NoteView(ModelView):
    can_create = False  # disable model deletion
    can_edit = False  # disable model deletion
    can_delete = False  # disable model deletion
    can_export = True  # allows export of data as a spreadsheet
    page_size = 25  # the number of entries to display on the list view
    column_list = (
        'user_id', 'league.league_name', 'data', 'date')
    column_searchable_list = [
        'user_id', 'league.league_name', 'data', 'date']

    def is_accessible(self):
        return current_user.id == 3


# Custom ModelView
class MemberView(ModelView):
    can_create = False  # disable model deletion
    can_edit = False  # disable model deletion
    can_delete = False  # disable model deletion
    can_export = True  # allows export of data as a spreadsheet
    page_size = 25  # the number of entries to display on the list view
    column_list = (
        'user_id', 'league.league_name', 'member_name', 'member_role',
        'title.title_name')
    column_searchable_list = [
        'user_id', 'league.league_name', 'member_name', 'member_role',
        'title.title_name']

    def is_accessible(self):
        return current_user.id == 3

    # If another user goes directly to a url like /admin/user
    # This redirects them to the home screen
    def inaccessible_callback(self, name, **kwargs):
        flash("You are not the Admin!", category="warning")
        return redirect(url_for("home"))


# Add administrative views here
admin.add_view(UserView(User, db.session))
admin.add_view(LeagueView(League, db.session))
admin.add_view(TitleView(Title, db.session))
admin.add_view(MemberView(Member, db.session))
admin.add_view(NoteView(Note, db.session))
