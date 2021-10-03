#IMPORT THE FLASK OBJECT WHICH THE APP WILL BE AN INSTANCE OF AND THE CONFIG CLASS 
from flask import Flask
from config import Config

#import Blueprints
from .community.routes import community
from .authorization.routes import auth

#import database
from .models import db, login
from flask_migrate import Migrate, migrate

#instance of the application
app = Flask(__name__)

#Blueprint Registration
app.register_blueprint(community)
app.register_blueprint(auth)

#configure the app form the config file
app.config.from_object(Config)

#config database
db.init_app(app)

migrate = Migrate(app,db)
#where to find the routes

#config login manager
login.init_app(app)

from . import routes
from . import models
