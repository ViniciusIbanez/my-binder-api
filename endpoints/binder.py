from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets
from helpers.binders.binder_helper import *
from helpers.binders.binder_helper import *
import json

class Binder(Resource):

    def post(self):
        cards_object = request.get_json()
        secrets = retrieve_secrets()
        mongo_connection = connect(credentials=secrets, collection='Binders')
        response = insert_cards(cards_object, mongo_connection)
        if response:
            return jsonify(code = 200, data={"message": "Cards Succesfully Inserted to Binder"})
        else:
            return jsonify(code = 403)

class RetrieveBinder(Resource):

    def post(self):
            user_id = request.get_json().get('user')
            secrets = retrieve_secrets()
            mongo_connection = connect(credentials=secrets, collection='Binders')
            cards_list = retrieve_cards_from_user(user_id, mongo_connection)
            mongo_connection = connect(credentials=secrets, collection='Cards')
            cards = retrieve_cards_by_id(cards_list, mongo_connection)
        
            if cards:
                return jsonify(code = 200, body={"cards": cards})
            else:
                return jsonify(code = 403)

class InsertCard(Resource):

    def post(self):
        request_data = request.get_json()
        user_id = request_data.get('user')
        card_id = request_data.get('card_id')
        secrets = retrieve_secrets()
        binders_connection = connect(credentials=secrets, collection='Binders')
        card_object = {
            'user': user_id,
            'cards': [card_id]
        }

        insert_cards(card_object, binders_connection)

        if insert_cards:
            return  jsonify(code = 200)
        else:
            return jsonify(code = 403)