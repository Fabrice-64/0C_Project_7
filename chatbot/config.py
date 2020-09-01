from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):

    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    FLASK_APP = os.environ.get("chatbot.py")
