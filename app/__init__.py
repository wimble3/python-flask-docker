from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from flask import Flask

from flask_cors import CORS

from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from settings import HOST, REDIS_PORT, REDIS_DB, SQLALCHEMY_DATABASE_URI, SECRET_KEY


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = SECRET_KEY
CORS(app)

# Adding SQLAlchemy
db = SQLAlchemy(app)
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Adding marshmallow
ma = Marshmallow(app)

# Adding redis
redis = Redis(host=HOST, port=REDIS_PORT, db=REDIS_DB)

# Routing
from management.server import bp as bp__server  # noqa: E402
app.register_blueprint(bp__server)
from management.telethon import bp as bp__telethon  # noqa: E402
app.register_blueprint(bp__telethon)
from app.api.auth.views import bp as bp__auth  # noqa: E402
app.register_blueprint(bp__auth)

# Events
from app.telegram.telethon.events import *  # noqa: F401

# Adding swagger routing
from app.swagger_ui.views import (bp as swagger, swagger_ui_blueprint as swagger_ui)  # noqa: E402, I100, E501
app.register_blueprint(swagger)
app.register_blueprint(swagger_ui)
