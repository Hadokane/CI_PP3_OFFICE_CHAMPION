from officechampion import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# creates the User login table
# user mixin used from flask
class User(db.Model, UserMixin):
    # generated Id that will be used as the Primary Key
    id = db.Column(db.Integer, primary_key=True)
    # unique means only one instance of each username may exist,
    # nullable false means it can't be left blank
    username = db.Column(db.String(300), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    # tells the table there is a relationship with the notes table
    # every time a note is created, sql adds the note id to the user
    # storing all the data associated with the user
    # one-to-many relationship (one user, many notes)
    # here sql wants the name capital the same as the class name
    # cascade finds all related tasks & deletes them
    # lazy finds all related notes while searching tables
    notes = db.relationship(
        "Note", backref="user", cascade="all, delete", lazy=True)
    # relationship with League table
    leagues = db.relationship(
        "League", backref="user", cascade="all, delete", lazy=True)
    # relationship with Title table
    titles = db.relationship(
        "Title", backref="user", cascade="all, delete", lazy=True)
    # relationship with Members table
    members = db.relationship(
        "Member", backref="user", cascade="all, delete", lazy=True)

    # represent itself as a string
    def __repr__(self):
        return f"#{self.id} - Data: {self.username} - Date: {self.password}"


# creates a test note table to give the user something to do
# will be replaced by the relevant tables once functionality is tested
# ensures users can login, create note, logout, login, see notes
class Note(db.Model):
    # generated Id that will be used as the Primary Key
    id = db.Column(db.Integer, primary_key=True)
    # 5000 character text data
    data = db.Column(db.Text, nullable=False)
    # uses func to get the current date and time and store it on creation
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # foreign key used to associate a note with the specific user object
    # name is lowercase due to sql conventions
    # CASCADE - if user is deleted, linked notes are also deleted
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"))
    # foreign key used to associate a note with a specific league
    league_id = db.Column(db.Integer, db.ForeignKey(
        "league.id", ondelete="CASCADE"))

    # represent itself as a string
    def __repr__(self):
        return f"#{self.id} - Data: {self.data} - Date: {self.date}"


# creates a table to store the leagues
class League(db.Model):
    # generated Id that will be used as the Primary Key
    id = db.Column(db.Integer, primary_key=True)
    # 50 character limit
    league_name = db.Column(db.String(50), nullable=False)
    # foreign key used to associate a league with a specific user
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"))
    # relationship with Title table
    titles = db.relationship(
        "Title", backref="league", cascade="all, delete", lazy=True)
    # relationship with Members table
    members = db.relationship(
        "Member", backref="league", cascade="all, delete", lazy=True)
    # relationship with Notes table
    notes = db.relationship(
        "Note", backref="league", cascade="all, delete", lazy=True)

    # represent itself as a string
    def __repr__(self):
        return f"#{self.id} - League Name: {self.league_name}"


# creates a table to store the titles
class Title(db.Model):
    # generated Id that will be used as the Primary Key
    id = db.Column(db.Integer, primary_key=True)
    # title name - 100 character limit
    title_name = db.Column(db.String(100), nullable=False)
    # title description
    title_description = db.Column(db.Text, nullable=False)
    # date title created
    title_created = db.Column(db.Date, nullable=False)
    # external_img_url (can't store images directly in db)
    image_url = db.Column(db.String(500))
    # foreign key used to associate a title with the specific user
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=False)
    # foreign key used to associate a title with a specific league
    league_id = db.Column(db.Integer, db.ForeignKey(
        "league.id", ondelete="CASCADE"), nullable=False)
    # relationship with Members table
    members = db.relationship(
        "Member", backref="title", cascade="all, delete", lazy=True)

    # represent itself as a string
    def __repr__(self):
        return self


# creates a table to store members
class Member(db.Model):
    # generated Id that will be used as the Primary Key
    id = db.Column(db.Integer, primary_key=True)
    # member name
    member_name = db.Column(db.String(100), nullable=False)
    # member role (in group, i.e. job, gaming role, sports position etc.)
    member_role = db.Column(db.Text, nullable=False)
    # external_img_url (can't store images directly in db)
    member_image = db.Column(db.String(500))
    # date title won
    champion_for = db.Column(db.Date, nullable=False)
    # foreign key used to associate a member with the specific user
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=False)
    # foreign key used to associate a member with a specific league
    league_id = db.Column(db.Integer, db.ForeignKey(
        "league.id", ondelete="CASCADE"), nullable=False)
    # foreign key used to associate a member with a specific title
    title_id = db.Column(db.Integer, db.ForeignKey(
        "title.id", ondelete="CASCADE"), nullable=False)

    # represent itself as a string
    def __repr__(self):
        return self
