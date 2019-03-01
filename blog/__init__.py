import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
#app.config["SQLALCHEMY_DATABASE_URI"] =\
#    "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLAlCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from blog import routes # To avoid circular imports