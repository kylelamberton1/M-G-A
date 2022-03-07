from application import app, db, bcrypt
from application.models import User, Movie
from application.forms import AddForm, UpdateForm, SignupForm, LoginForm, AccountupdateForm, AccountdeleteForm
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home():
    print(current_user)
    return render_template('home.html', title='Home')

    
@app.route('/signup', methods=['GET','POST'])
def signup():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
   
    signupform = SignupForm()
    if signupform.validate_on_submit():
	
        hash_password = bcrypt.generate_password_hash(signupform.password.data)
        user = User (username=signupform.username.data, password=hash_password)
	
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('signup.html', title='Signup', form=signupform)


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    loginform = LoginForm()
   
    if loginform.validate_on_submit():
        user=User.query.filter_by(email=loginform.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, loginform.password.data):
            login_user(user, remember=loginform.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=loginform)


@app.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('login'))


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    addform = AddForm()
    if addform.validate_on_submit():
        name = Movie(director_name=addform.director_name.data, title=addform.title.data, genre=addform.genre.data, plot_summary=addform.plot_summary.data, user_id = current_user.id)
        db.session.add(name)
        db.session.commit()
        return redirect(url_for('read'))   
    return render_template('add.html', title='Add', form=addform)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    
    userform = AccountupdateForm()
    
    delete_account = AccountdeleteForm()
    
    
    if userform.validate_on_submit():
        current_user.username = userform.username.data
        current_user.password = userform.password.data
        db.session.commit()
        return redirect(url_for('account'))
   
    elif request.method == 'GET':
        userform.username.data = current_user.username
        userform.password.data = current_user.password
        
    
    if delete_account.is_submitted():
        user = User.query.filter_by(userID = current_user.userID).first()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('signup'))

    return render_template('account.html', title = 'Account', form = userform, delete = delete_account)


@app.route('/read', methods=['GET'])
@login_required
def read():
    reads = Movie.query.all()
    return render_template('read.html', title='Read', reads=reads)

@app.route('/update/<director_name>', methods=['GET', 'POST'])
@login_required
def update(director_name):
    updateform = UpdateForm()
    read = Movie.query.filter_by(director_name=director_name).first()
    if request.method == 'GET':
            updateform.director_name.data = read.director_name
            updateform.title.data = read.title
            updateform.genre.data = read.genre
            updateform.plot_summary.data = read.plot_summary
            return render_template('update.html', title='Update', form=updateform)
    else:
        if updateform.validate_on_submit():
            read.director_name = updateform.director_name.data
            read.title = updateform.title.data
            read.genre = updateform.genre.data
            read.plot_summary = updateform.plot_summary.data
            db.session.commit()
            return redirect(url_for('read'))

@app.route('/delete/<director_name>', methods=['GET', 'POST'])
@login_required
def delete(director_name):
        read = Movie.query.filter_by(director_name=director_name).first()
        db.session.delete(read)
        db.session.commit()
        return redirect(url_for('read'))


    