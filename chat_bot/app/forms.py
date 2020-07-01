from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class SearchForm(FlaskForm):
    # Validator InputRequired is recommended by wtforms.
    address_search = StringField("Quel lieu t'intéresse ?", [InputRequired()])
