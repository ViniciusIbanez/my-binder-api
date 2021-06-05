from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets
from helpers.user_helper import *
from helpers.binders.binder_helper import insert_cards
from helpers.binders.binder_helper import *
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


class  UserInit(Resource):
    
    def post(self):
        request_data = request.get_json()
        user  = request_data.get("user")
        secrets = retrieve_secrets()

        user_connection =connect(credentials=secrets, collection='User')
        
        try:
            print(f'## USER INIT')
            user_response  = insert_user({'user': user}, user_connection)
            if user_response:
                binder_connection =  connect(credentials=secrets, collection='Binder')
                cards_list = retrieve_cards_from_user(user, binder_connection)
                print(f'## USER BINDER: {cards_list}')
                if cards_list:
                    cards_connection =  connect(credentials=secrets, collection='Cards') 
                    cards = retrieve_cards_by_id(cards_list, cards_connection)
                    print(f'## CARDS: {cards}')
                    if cards:
                         return jsonify(code = 200, body={"cards": cards})
            else:
                return jsonify(code = 403)
        except Exception as e:
            print(f"## ERROR: {e}")

