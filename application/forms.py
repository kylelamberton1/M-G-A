from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class AddDirectorForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=2,max=20)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Submit')

class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1,max=100)])
    genre = StringField('Genre', validators=[DataRequired(), Length(min=2,max=25)])
    plot_summary = StringField('Plot Summary', validators=[DataRequired(), Length(min=1,max=1000)])
    submit = SubmitField('Submit')



'''
class UpdateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    completed = BooleanField('Completed')
    submit = SubmitField('Update')'''