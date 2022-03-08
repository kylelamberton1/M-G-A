from application.models import db, Movie, User

db.drop_all()
db.create_all()