from flask import Flask
from config import Config, NLTKData


app = Flask(__name__)


app.config.from_object(Config)
nltk = NLTKData()
NLTK_DATA = nltk.get_path_nltk_data()


from app import routes

