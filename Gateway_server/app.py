from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# main driver function
if __name__ == '__main__':
    print('in run')
    app.run(debug=True,port=5000)

swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    '/static/swagger.json',
    config={
        'app_name': 'Flash-Card-App'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')

import gateway