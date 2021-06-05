from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from endpoints.cards_etl import *
from endpoints.user import *
from endpoints.binder import *

app = Flask(__name__)
api = Api(app)


api.add_resource(CardsEtl, '/extract/set')
api.add_resource(User, '/user/insert')
api.add_resource(Binder, '/binder/insert-card')
api.add_resource(RetrieveBinder, '/binder/retrieve')
api.add_resource(InsertRandom, '/card/insert-random')
api.add_resource(UserInit, '/user/init')

if __name__ == '__main__':
    app.run(debug=True)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)