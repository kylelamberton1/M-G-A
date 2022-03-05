from application import app, db
from application.models import Movie
from application.forms import AddForm, UpdateForm
from flask import render_template, redirect,url_for, request

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

@app.route('/update/<director_name>', methods=['GET', 'POST'])
def update(director_name):
    updateform = UpdateForm()
    read = Movie.query.filter_by(director_name=director_name).first()
    if request.method == 'GET':
            updateform.director_name.data = read.director_name
            updateform.title.data = read.title
            updateform.genre.data = read.genre
            updateform.plot_summary.data = read.plot_summary
            return render_template('update.html', form=updateform)
    else:
        if updateform.validate_on_submit():
            read.director_name = updateform.director_name.data
            read.title = updateform.title.data
            read.genre = updateform.genre.data
            read.plot_summary = updateform.plot_summary.data
            db.session.commit()
            return redirect(url_for('read'))

@app.route('/delete/<director_name>', methods=['GET', 'POST'])
def delete(director_name):
        read = Movie.query.filter_by(director_name=director_name).first()
        db.session.delete(read)
        db.session.commit()
        return redirect(url_for('read'))
    