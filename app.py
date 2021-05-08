from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets
from etl.extract_cards import *

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        secrets = retrieve_secrets()
        print(f'Secrets: {secrets}')
        mongo_connection  = connect(credentials=secrets, collection='Cards')
        print(f'Mongo Connection: {mongo_connection}')
        
        cards = []
        for card in mongo_connection.find({}):
            id = str(card.pop('_id'))
            card['id'] = id
            cards.append(card)
        return  jsonify(code=200, data=cards)

class ExtractLoad(Resource):
    def post(self):
        request_data = request.get_json()
        set_code = request_data['set_code']
        secrets = retrieve_secrets()
        mongo_connection = connect(credentials=secrets, collection='Cards')
        set_cards = extract_set(set_code)
        response = load_set(set_cards, )
        
        return jsonify(code = 200 , data=response)
        


api.add_resource(HelloWorld, '/cards/all')
api.add_resource(ExtractLoad, '/extract/set')
if __name__ == '__main__':
    app.run(debug=True)