from flask import Flask
from config import Config




app = Flask(__name__) #app is an instance of Flask
app.config.from_object(Config) #app, configure smth from the class Config

from app import routes




