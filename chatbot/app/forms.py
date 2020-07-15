from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class Question(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
