from flask import render_template, url_for, request 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

from app import app, db
from app.models import Users, Books
from app.forms import Bookform

#homepage

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def home():
    error = ""
    return 'Homepage'

#about us page 

@app.route('/about')
def about():
    return 'About us!'

#sign in 

@app.route('/signin', method = ['GET', ['POST'])
def signin ():
    error = ""
    form = Userform 

    if request.method == 'POST':
        username = form.username.data
        books = form.books.data

        if len(username) == 0:
            error = "Please enter name"
        else: 
            return "You're in!"
        
        return render_template ('home.html', form=form, message = error) 

#add books view 

@app.route('/add', methods=['POST', 'GET'])
def add_book():
    error = ""
    form = Bookform()
    if form.validate_on_submit():
        book_name = form.book_name.data
        author_name = form.author_name.data
        book_review = form.book_review.data 

        book = Book (book_name = book_name , author_name = author_name , book_review = book_review)
        
        db.session.add(book)
        db.session.commit()

    return render_template('add.html', form=form, message = error)

#read 



#update book review

@app.route ('/update', methods=['GET', 'POST'])
def update (review):
    error = ""
    form = Bookform 
    Boo
    book.complete = True
    db.session.commit()
    return redirect(url_for('home.html'))


#delete 






