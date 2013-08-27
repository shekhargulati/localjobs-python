from flask import Flask
import pymongo
from pymongo import MongoClient
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = 'secret_key'

client = MongoClient('localhost', 27017)
db = client['localjobs']

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'signin'


from app import views , models