from application import db


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(30))
    movie = db.relationship('Movie', backref='director', lazy='joined')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre = db.Column(db.String(25))
    plot_summary = db.Column(db.String(1000))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))


