from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productDb.sqlite3'
app.config['SQLALCEMY_TRACK_MODIFICATIONS']= False

ma  = Marshmallow(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    '/static/swagger.json',
    config={
        'app_name': 'Flash-Card-App'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')


import routes , model


