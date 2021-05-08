from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets
from helpers.extract_cards import *

class CardsEtl(Resource):

    def post(self):
        request_data = request.get_json()
        set_code = request_data['set_code']
        secrets = retrieve_secrets()
        mongo_connection = connect(credentials=secrets, collection='Cards')
        set_cards = extract_set(set_code)
        response = load_set(set_cards, mongo_connection)

        if response:
            return jsonify(code = 200, data={"message": "Cards Succesfully Extracted"})
        else:
            return jsonify(code = 403)