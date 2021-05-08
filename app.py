from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from endpoints.cards_etl import *

app = Flask(__name__)
api = Api(app)


api.add_resource(CardsEtl, '/extract/set')
if __name__ == '__main__':
    app.run(debug=True)