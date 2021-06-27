from application import db 

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    books = db.relationship ('Books', backref = "user")

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user id'), nullable=False)
    book_name = db.Column(db.String(50), nullable=False)
    author_name = db.Column(db.string(30))
    book_review = db.Column(db.String(500))



