from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint



app = Flask(__name__)

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userDb.sqlite3'
app.config['SQLALCEMY_TRACK_MODIFICATIONS']= False

swaggerui_blueprint = get_swaggerui_blueprint(
    Config.SWAGGER_URL,
    Config.API_URL,
    config={
        'app_name': 'Flash-Card-App'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=Config.SWAGGER_URL)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import routes , models
