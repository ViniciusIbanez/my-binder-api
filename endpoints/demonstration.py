from flask_restful import Resource, Api
from flask import Flask, jsonify, request
import json

class Demonstration(Resource):

    def get(self):
        
        message = "Olá Mundo"
        if message:
           return jsonify(code = 200, body={"data": message})
        else:
            return jsonify(code = 404)

    def post(self):
        request_data = request.get_json()
        print(f'## Request Payload: {request_data}')
        user_card  =  request_data['user']
        white_list = ['1302222130']
        if user_card in white_list:
            message = f'Acesso liberado para o cartao {user_card} !! '
            return jsonify(code = 200, body={"data": message})
        else:
            message = f'Cartão {user_card} nao cadastrado !! '
            return jsonify(code = 403, body={"data": message})