from application import db
from application.models import Director

db.drop_all()
db.create_all()