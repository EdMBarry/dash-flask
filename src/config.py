import os


DB_PATH=os.path.join(os.path.dirname(__file__), 'database.db')
SECRET_KEY = 'mysecret'
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
