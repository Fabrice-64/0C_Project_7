import os
import secure_keys

class Config(object):
    SECRET_KEY = secure_keys.SECRET_KEY

    GOOGLE_API_KEY = secure_keys.GOOGLE_API_KEY
