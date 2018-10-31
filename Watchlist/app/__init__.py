from flask import Flask
from .config import DevConfig

#Initializing application
app = Flask (__name__, instance_relative_config=True)   # instance_relative_config allows us to connect to the instance folder when the app instance is created

#Set up configuration
app.config.from_object(DevConfig)    #app.config.from_object() method is used to setup the configuration using the DecConfig class which is passed in.
app.config.from_pyfile('config.py')  #app.config.from_pyfile('config.py') connects to config.py and all its contents are appended to the app.config

from app import views