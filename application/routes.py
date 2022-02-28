from application import app, db
from application.models import Director, Movie
from application.forms import AddForm
from flask import render_template

@app.route('/add', methods=['GET', 'POST'])
def add():
    addform = AddForm()
    if addform.validate_on_submit():
        name = Director, Movie(first_name=addform.first_name.data, last_name=addform.last_name.data)
        db.session.add(name)
        db.session.commit()
    return render_template('add.html', form=addform)

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    read = Director, Movie.query.all()
    return render_template('read.html', read=read)


    