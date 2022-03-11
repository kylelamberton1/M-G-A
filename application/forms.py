from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from application import bcrypt
from application.models import User
from wtforms.validators import DataRequired, Length, ValidationError


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2,max=100)])
    submit = SubmitField('Submit')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already in use, please choose another')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2,max=100)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')

    def validate_details(self, username, password):
        user = User.query.filter_by(username=username.data).first()

        if user is None:
            raise ValidationError('Username is not recognised')

        if bcrypt.check_password_hash(user.password, password.data):
            raise ValidationError('Incorrect password, please try again')
            



class AccountupdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2,max=100)])
    submit = SubmitField('Submit')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already in use, please choose another')


class AccountdeleteForm(FlaskForm):
    delete = SubmitField('Delete Account')


class AddForm(FlaskForm):
    director_name = StringField('Director Name', validators=[DataRequired(), Length(min=2,max=60)])
    title = StringField('Title', validators=[DataRequired(), Length(min=1,max=100)])
    genre = StringField('Genre', validators=[DataRequired(), Length(min=2,max=25)])
    plot_summary = StringField('Plot Summary', validators=[DataRequired(), Length(min=1,max=1000)])
    submit = SubmitField('Submit')


class UpdateForm(FlaskForm):
    director_name = StringField('Director Name', validators=[DataRequired(), Length(min=2,max=60)])
    title = StringField('Title', validators=[DataRequired(), Length(min=1,max=100)])
    genre = StringField('Genre', validators=[DataRequired(), Length(min=2,max=25)])
    plot_summary = StringField('Plot Summary', validators=[DataRequired(), Length(min=1,max=1000)])
    submit = SubmitField('Subbmit'


