from application import db
from application.models import Movie

db.drop_all()
db.create_all()