from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///OrderDb.sqlite3'
app.config['SQLALCEMY_TRACK_MODIFICATIONS']= False

ma  = Marshmallow(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import cart , model , orders_history


