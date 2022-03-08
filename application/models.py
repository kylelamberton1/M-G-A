from application import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False,)
    password = db.Column(db.String(100), nullable=False)
    movie = db.relationship('Movie', backref='user', lazy=True)

    def __repr__(self):
        return ''.join(['User ID: ', str(self.username)])

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    director_name = db.Column(db.String(60), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(25), nullable=False)
    plot_summary = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return ''.join(['Director Name: ', str(self.director_name), '\r\n',
                        'Title: ', str(self.title), '\r\n',
                        'Genre: ', str(self.genre), '\r\n',
                        'Plot Summary: ', str(self.plot_summary), '\r\n',])
    


