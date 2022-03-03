from application import app, db
from application.models import Director, Movie
from application.forms import AddDirectorForm, AddMovieForm
from flask import render_template, redirect, url_for

@app.route('/add_director', methods=['GET', 'POST'])
def add_director():
    add_d_form = AddDirectorForm()
    if add_d_form.validate_on_submit():
        name = Director(first_name=add_d_form.first_name.data, last_name=add_d_form.last_name.data)
        db.session.add(name)
        db.session.commit()
        return redirect(url_for('add_movie'))
    return render_template('add_director.html', form=add_d_form)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    add_m_form = AddMovieForm()
    if add_m_form.validate_on_submit():
        name = Movie(title=add_m_form.title.data, genre=add_m_form.genre.data, plot_summary=add_m_form.plot_summary.data)
        db.session.add(name)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('add_movie.html', form=add_m_form)


@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    read = db.session.query(Movie, Director).join(Director, Movie.id == Director.id).all()

    return render_template('read.html', read=read)

@app.route('/delete/<entry>', methods=['GET', 'POST'])
def delete(entry):
    name = db.session.query(Movie,Director).filter_by(entry=entry).first()
    db.session.delete(name)
    db.session.commit()
    return redirect(url_for('read'))






'''    
@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    read = Director.query.all()
    return render_template('read.html', read=read)

'''

'''
read = Movie.query.all()
name = Movie(title=addform.title.data, genre=addform.genre.data, plot_summary=addform.plot_summary.data)
'''