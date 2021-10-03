#IMPORT THE FLASK OBJECT WHICH THE APP WILL BE AN INSTANCE OF AND THE CONFIG CLASS 
from flask import Flask
from config import Config

#import Blueprints
from .community.routes import community

#import database
from .models import db
from flask_migrate import Migrate, migrate

#instance of the application
app = Flask(__name__)

#Blueprint Registration
app.register_blueprint(community)

#configure the app form the config file
app.config.from_object(Config)

#config database
db.init_app(app)

migrate = Migrate(app,db)
#where to find the routes
from . import routes
from . import models
