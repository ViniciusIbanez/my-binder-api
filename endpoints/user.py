from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets
from helpers.user_helper import *

class User(Resource):

    def post(self):
        request_data = request.get_json()
        user= request_data['user']
        secrets = retrieve_secrets()
        mongo_connection = connect(credentials=secrets, collection='User')
        response = insert_user(request_data, mongo_connection)

        return {"deu" : "certo"}