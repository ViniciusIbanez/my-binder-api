from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets
from helpers.user_helper import *
from helpers.binders.binder_helper import insert_cards
import logging

class User(Resource):

    def post(self):
        request_data = request.get_json()
        user = request_data.get("user")
        secrets = retrieve_secrets()
        mongo_connection = connect(credentials=secrets, collection='User')
        response = insert_user({'user': user}, mongo_connection)

        # will be removed in the near future 
        binders_connection = connect(credentials=secrets, collection='Binders')
        cards_object = {
            'user': user,
            'cards': ["438567", "438570", "438571"]
        }
        insert_cards(cards_object, binders_connection)

        if cards_object:
            return  jsonify(code = 200)
        else:
            return jsonify(code = 403)