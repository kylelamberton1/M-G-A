from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, ValidationError

class AddForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=2,max=20)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=2,max=30)])
    title = StringField('Title', validators=[DataRequired(), Length(min=1,max=100)])
    genre = StringField('Genre', validators=[DataRequired(), Length(min=2,max=25)])
    age_rating = IntegerField('Age Rating', validators=[DataRequired(), Length(min=1,max=2)])
    budget_in_millions = DecimalField('Budget (millions)', validators=[DataRequired(), Length(min=1,max=9)])
    plot_summary = StringField('Plot Summary', validators=[DataRequired(), Length(min=1,max=1000)])
    submit = SubmitField('Submit')



'''
class UpdateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    completed = BooleanField('Completed')
    submit = SubmitField('Update')'''