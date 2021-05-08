from flask import Flask, jsonify
from flask_restful import Resource, Api
from connectors.mongo import connect
from helpers.secrets_helper import retrieve_secrets

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
        


api.add_resource(HelloWorld, '/cards/all')

if __name__ == '__main__':
    app.run(debug=True)