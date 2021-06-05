from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets
from helpers.binders.binder_helper import *
from helpers.binders.binder_helper import *
import json

class Card(Resource):

    def post(self):
        
        secrets = retrieve_secrets()
        mongo_connection = connect(credentials=secrets, collection='Cards')
        cards = retrieve_all_cards(mongo_connection)
        print(f'CARDS: {cards}')
        if cards:
           return jsonify(code = 200, body={"cards": cards})
        else:
            return jsonify(code = 403)