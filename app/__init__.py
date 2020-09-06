from flask import Flask
from config import Config
import nltk


app = Flask(__name__)


app.config.from_object(Config)
nltk.download('punkt')

from app import routes

