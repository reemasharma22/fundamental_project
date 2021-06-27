from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, TextAreaField


class Bookform(FlaskForm):
    book_name = StringField ('Name of book')
    author_name = StringField ('Author')
    book_review = TextAreaField('Book Review')
    submit = SubmitField('Add review')

class Userform(FlaskForm):
    username = StringField ('Name of customer')
    books = StringField ('Name of book')