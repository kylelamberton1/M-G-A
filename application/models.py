from application import db


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(30))
    Movie = db.relationship('Movie', backref='Director')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre = db.column(db.String(25))
    age_rating = db.Column(db.Integer)
    budget_in_millions = db.Column(db.Float)
    plot_summary = db.Column(db.String(1000))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)


