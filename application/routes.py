from application import app, db
from application.models import Movie
from application.forms import AddForm
from flask import render_template, redirect,url_for

@app.route('/add', methods=['GET', 'POST'])
def add():
    addform = AddForm()
    if addform.validate_on_submit():
        name = Movie(director_name=addform.director_name.data, title=addform.title.data, genre=addform.genre.data, plot_summary=addform.plot_summary.data)
        db.session.add(name)
        db.session.commit()
        return redirect(url_for('read'))   
    return render_template('add.html', form=addform)

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    reads = Movie.query.all()
    return render_template('read.html', reads=reads)


    