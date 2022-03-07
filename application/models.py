from application import db


'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(150))
    password = db.Column(db.String(100))
    movie = db.relationship('Movie', backref='user', lazy=True)
'''
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    director_name = db.Column(db.String(60))
    title = db.Column(db.String(100))
    genre = db.Column(db.String(25))
    plot_summary = db.Column(db.String(1000))
    


