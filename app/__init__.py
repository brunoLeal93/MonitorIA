from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('config')


Bootstrap(app)
db = MongoEngine(app)
lm = LoginManager()
lm.init_app(app)


from app.controllers import main



