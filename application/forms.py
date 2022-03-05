from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

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
    submit = SubmitField('Submit')


