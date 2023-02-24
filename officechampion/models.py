from officechampion import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# creates the User login table
# user mixin used from flask
class User(db.Model, UserMixin):
    # generated Id that will be used as the Primary Key
    id = db.Column(db.Integer, primary_key=True)
    # unique means only one instance of each username may exist,
    # max string of 25 characters allowed but set to 30 for safety
    # nullable false means it can't be left blank
    username = db.Column(db.String(30), unique=True, nullable=False)
    # max string of 25 characters allowed but set to 30 for safety
    password = db.Column(db.String(30), nullable=False)
    # tells the table there is a relationship with the notes table
    # every time a note is created, sql adds the note id to the user
    # storing all the data associated with the user
    # one-to-many relationship (one user, many notes)
    # here sql wants the name capital the same as the class name
    notes = db.relationship("Note", backref="user")

    # represent itself as a string
    def __repr__(self):
        return self


# creates a test note table to give the user something to do
# will be replaced by the relevant tables once functionality is tested
# ensures users can login, create note, logout, login, see notes
class Note(db.Model):
    # generated Id that will be used as the Primary Key
    id = db.Column(db.Integer, primary_key=True)
    # 5000 character text data
    data = db.Column(db.String(5000))
    # uses func to get the current date and time and store it on creation
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # foreign key used to associate a note with the specific user object
    # name is lowercase due to sql conventions
    # CASCADE - if user is deleted, linked notes are also deleted
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"))

    # represent itself as a string
    def __repr__(self):
        return f"#{note.id} - Data: {note.data} - Date: {note.date}"
