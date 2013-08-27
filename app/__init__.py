from flask import Flask
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = 'secret_key'

client = MongoClient('localhost', 27017)
db = client['localjobs']

from app import views , models