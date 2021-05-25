from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from endpoints.cards_etl import *
from endpoints.user import *

app = Flask(__name__)
api = Api(app)


api.add_resource(CardsEtl, '/extract/set')
api.add_resource(User, '/user/insert')
if __name__ == '__main__':
    app.run(debug=True)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)