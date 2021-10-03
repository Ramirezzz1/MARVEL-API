# os is a built in python module that lets us do some operating system operations
import os 

#need to tell flask where the root directory for the project is 
basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """
    Configuration variables !
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False