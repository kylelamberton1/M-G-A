from application import db

    

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    director_name = db.Column(db.String(60))
    title = db.Column(db.String(100))
    genre = db.Column(db.String(25))
    plot_summary = db.Column(db.String(1000))
    


