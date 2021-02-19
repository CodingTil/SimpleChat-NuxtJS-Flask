from flask import Flask
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)

api = Api(app)
jwt = JWTManager(app)

app.config.from_pyfile('.env')
app.config['PROPAGATE_EXCEPTIONS'] = True

initialize_db(app)
initialize_routes(api)

app.run(host='0.0.0.0', debug='true')