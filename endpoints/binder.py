from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets
from helpers.binders.binder_helper import *

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